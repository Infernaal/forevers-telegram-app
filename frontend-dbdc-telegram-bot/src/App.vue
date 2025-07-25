<template>
    <div class="min-h-screen bg-white telegram-webapp container-responsive touch-optimized">
        <RouterView />
    </div>
</template>

<script>
    import { onMounted } from 'vue'

    export default {
        name: 'App',
        setup() {
            onMounted(() => {
                // Telegram WebApp configuration
                if (window.Telegram && window.Telegram.WebApp) {
                    const webapp = window.Telegram.WebApp
                    webapp.ready()
                    webapp.expand()
                    webapp.disableVerticalSwipes()

                    // Set theme colors
                    webapp.setHeaderColor('#FFFFFF')
                    webapp.setBackgroundColor('#FAFAFA')
                }

                // Prevent zoom on mobile
                const viewport = document.querySelector('meta[name="viewport"]')
                if (!viewport) {
                    const meta = document.createElement('meta')
                    meta.name = 'viewport'
                    meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover'
                    document.head.appendChild(meta)
                }

                // Set viewport height for mobile
                const setViewportHeight = () => {
                    document.documentElement.style.setProperty('--vh', `${window.innerHeight * 0.01}px`)
                }
                setViewportHeight()
                window.addEventListener('resize', setViewportHeight)
                window.addEventListener('orientationchange', setViewportHeight)
            })
        }
    }
</script>

<style>
    /* Telegram WebApp viewport height */
    .telegram-webapp {
        height: 100vh;
        height: calc(var(--vh, 1vh) * 100);
        min-height: 100vh;
        min-height: calc(var(--vh, 1vh) * 100);
    }

    /* Prevent overscroll bouncing and optimize for touch */
    .telegram-webapp {
        overscroll-behavior: none;
        -webkit-overflow-scrolling: touch;
        -webkit-tap-highlight-color: transparent;
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

        /* Allow text selection for content elements */
        .telegram-webapp input,
        .telegram-webapp textarea,
        .telegram-webapp [contenteditable],
        .text-selectable {
            -webkit-user-select: text;
            -moz-user-select: text;
            -ms-user-select: text;
            user-select: text;
        }

    /* Responsive container adjustments */
    @media (max-width: 374px) {
        .telegram-webapp {
            font-size: 14px;
        }
    }

    @media (min-width: 768px) {
        .telegram-webapp {
            background: #f5f5f5;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
    }

    @media (min-width: 1024px) {
        .telegram-webapp {
            padding: 40px;
        }
    }

    /* Safe area support */
    @supports (padding: max(0px)) {
        .telegram-webapp {
            padding-top: max(0px, env(safe-area-inset-top));
            padding-bottom: max(0px, env(safe-area-inset-bottom));
            padding-left: max(0px, env(safe-area-inset-left));
            padding-right: max(0px, env(safe-area-inset-right));
        }
    }
</style>