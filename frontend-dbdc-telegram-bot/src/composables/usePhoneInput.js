import { computed, watch } from 'vue'
import { parsePhoneNumberFromString } from 'libphonenumber-js'
import { PhoneNumberUtil } from 'google-libphonenumber'

// Инициализация Google PhoneNumberUtil
const phoneUtil = PhoneNumberUtil.getInstance()

function getMaxLengthForCountry(iso2) {
  try {
    const meta = phoneUtil.getMetadataForRegion(iso2)
    if (!meta) return 15

    let lengths = []

    const collectLengths = (obj) => {
      if (obj?.possibleLength && Array.isArray(obj.possibleLength)) {
        lengths.push(...obj.possibleLength)
      }
    }

    collectLengths(meta.mobile)
    collectLengths(meta.fixedLine)

    if (!lengths.length) return 15

    // Считаем частоты длин
    const freqMap = lengths.reduce((acc, len) => {
      acc[len] = (acc[len] || 0) + 1
      return acc
    }, {})

    // Сортируем: сначала по частоте, потом по МЕНЬШЕЙ длине
    const sorted = Object.entries(freqMap)
      .map(([len, freq]) => ({ len: Number(len), freq }))
      .sort((a, b) => {
        if (b.freq === a.freq) {
          return a.len - b.len // при равной частоте берём меньшее
        }
        return b.freq - a.freq
      })

    return sorted[0].len
  } catch {
    return 15
  }
}

/**
 * Reusable phone input logic (length limits, validation, formatting, state flags).
 * @param {Ref} selectedCountry - ref({ name, code })
 * @param {Ref} formData - ref({ phone, ... })
 * @param {Ref} touchedFields - ref({ phone: boolean, ... })
 * @param {Ref} countries - ref(Array of country objects with name & phoneCode)
 */
export function usePhoneInput(selectedCountry, formData, touchedFields, countries) {
  const getSelectedCountryCode = () => {
    if (!selectedCountry.value.name) return 'Code'
    const country = countries.value.find(c => c.name === selectedCountry.value.name)
    return country ? country.phoneCode : 'Code'
  }

  const getPhonePlaceholder = () => {
    if (!selectedCountry.value.code) return 'Enter phone number'
    return 'Enter phone number'
  }

  const canEditPhone = computed(() => !!selectedCountry.value.code)

  const isPhoneValid = computed(() => {
    if (!selectedCountry.value.code || !formData.value.phone.trim()) return false
    const iso2 = selectedCountry.value.code.slice(0, 2).toUpperCase()
    const dial = getSelectedCountryCode().replace('+', '')
    try {
      const digitsOnly = formData.value.phone.replace(/\D/g, '')
      const fullIntl = `+${dial}${digitsOnly}`
      const parsed = parsePhoneNumberFromString(fullIntl)
      return !!parsed && parsed.country === iso2 && parsed.isValid()
    } catch {
      return false
    }
  })

  const displayPhoneNumber = computed(() => {
    if (!selectedCountry.value.code || !formData.value.phone) return formData.value.phone
    const dial = getSelectedCountryCode().replace('+', '')
    try {
      const digitsOnly = formData.value.phone.replace(/\D/g, '')
      const fullIntl = `+${dial}${digitsOnly}`
      const parsed = parsePhoneNumberFromString(fullIntl)
      if (parsed && parsed.isValid()) return parsed.formatInternational()
    } catch {}
    return `+${dial} ${formData.value.phone}`.trim()
  })

  const showPhoneCollapsed = computed(() => {
    return touchedFields.value.phone && formData.value.phone.trim().length > 0
  })

  const showPhoneFilled = computed(() => {
    return showPhoneCollapsed.value && isPhoneValid.value
  })

  const showPhoneError = computed(() => {
    if (!touchedFields.value.phone || !formData.value.phone.trim() || !selectedCountry.value.code) return false
    const hasContent = formData.value.phone.replace(/\D/g, '').length > 0
    const dial = getSelectedCountryCode().replace('+', '')
    try {
      const fullIntl = `+${dial}${formData.value.phone.replace(/\D/g, '')}`
      const parsed = parsePhoneNumberFromString(fullIntl)
      return hasContent && (!parsed || !parsed.isPossible())
    } catch {
      return hasContent
    }
  })

  const phoneOverLength = computed(() => {
    if (!selectedCountry.value.code) return false
    const iso2 = selectedCountry.value.code.slice(0, 2).toUpperCase()
    const digits = formData.value.phone.replace(/\D/g, '')
    const limit = getMaxLengthForCountry(iso2)
    return digits.length > limit
  })

  const phoneErrorMessage = computed(() => {
    if (phoneOverLength.value) return 'Phone number exceeds the maximum length for the selected country.'
    if (showPhoneError.value) return 'Please enter a valid phone number.'
    return ''
  })

    const handlePhoneInput = (event) => {
    if (!canEditPhone.value) {
        formData.value.phone = ''
        event.target.value = ''
        return
    }
    const iso2 = selectedCountry.value.code.slice(0, 2).toUpperCase()
    const limit = getMaxLengthForCountry(iso2)

    // Убираем всё, кроме цифр
    let digits = event.target.value.replace(/\D/g, '')

    // Режем только национальную часть
    const dialCode = getSelectedCountryCode().replace('+', '')
    if (digits.startsWith(dialCode)) {
        digits = digits.slice(dialCode.length)
    }
    digits = digits.slice(0, limit)

    formData.value.phone = digits
    event.target.value = digits
    }
    
  // Watcher для обрезки при вставке / автозаполнении
  watch(
    () => formData.value.phone,
    (newVal) => {
      if (!selectedCountry.value.code) return
      const iso2 = selectedCountry.value.code.slice(0, 2).toUpperCase()
      const limit = getMaxLengthForCountry(iso2)
      const digits = (newVal || '').replace(/\D/g, '').slice(0, limit)
      if (digits !== newVal) {
        formData.value.phone = digits
      }
    }
  )

  return {
    // state & validation
    isPhoneValid,
    displayPhoneNumber,
    showPhoneCollapsed,
    showPhoneFilled,
    canEditPhone,
    showPhoneError,
    phoneOverLength,
    phoneErrorMessage,
    // helpers
    getSelectedCountryCode,
    getPhonePlaceholder,
    // handlers
    handlePhoneInput
  }
}
