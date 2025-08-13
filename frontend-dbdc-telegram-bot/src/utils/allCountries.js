// Auto-generated country dataset using world-countries
// Provides: name.common, cca2, idd (root + suffixes)
import countries from 'world-countries'

function buildDialCode(idd) {
  if (!idd || !idd.root) return ''
  // Choose first suffix for representative dialing code
  if (idd.suffixes && idd.suffixes.length > 0) {
    return `+${idd.root.replace('+','')}${idd.suffixes[0]}`
  }
  return idd.root
}

// Generic phone digit assumptions per ITU E.164 (national significant number length 4-15)
// We'll set placeholder length 9 by default; can customize for known patterns.
function defaultDigitMeta(dial) {
  return { minDigits: 4, maxDigits: 15, placeholder: '123456789' }
}

export const fullCountries = countries.map(c => {
  const dial = buildDialCode(c.idd)
  const { minDigits, maxDigits, placeholder } = defaultDigitMeta(dial)
  return {
    name: c.name.common,
    code: c.cca2, // for flags
    phoneCode: dial || '+',
    minDigits,
    maxDigits,
    placeholder
  }
}).sort((a,b) => a.name.localeCompare(b.name))

export function findCountry(query) {
  if (!query) return null
  const q = query.toLowerCase()
  return fullCountries.find(c => c.code.toLowerCase() === q || c.name.toLowerCase() === q)
}
