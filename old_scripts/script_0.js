
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
              sans: ['Inter', 'sans-serif'],
              display: ['Space Grotesk', 'sans-serif'],
            },
            colors: {
              background: '#050505',
              surface: '#121212',
              'surface-highlight': '#1E1E1E',
              primary: '#ffffff',
              secondary: '#a1a1aa',
              accent: '#ccff00', 
            },
            animation: {
              'fade-in': 'fadeIn 0.5s ease-out',
              'slide-up': 'slideUp 0.5s ease-out',
              'marquee': 'marquee 140s linear infinite',
              'float': 'float 6s ease-in-out infinite',
              'spin-slow': 'spin 15s linear infinite',
              'pulse-fast': 'pulse 1.5s cubic-bezier(0.4, 0, 0.6, 1) infinite',
              'spin-medium': 'spin-medium 4s linear infinite',
            },
            keyframes: {
              fadeIn: {
                '0%': { opacity: '0' },
                '100%': { opacity: '1' },
              },
              slideUp: {
                '0%': { transform: 'translateY(20px)', opacity: '0' },
                '100%': { transform: 'translateY(0)', opacity: '1' },
              },
              marquee: {
                '0%': { transform: 'translateX(0)' },
                '100%': { transform: 'translateX(-50%)' },
              },
              float: {
                '0%, 100%': { transform: 'translateY(0)' },
                '50%': { transform: 'translateY(-15px)' },
              },
              'spin-medium': {
                '0%': { transform: 'rotate(0deg)' },
                '100%': { transform: 'rotate(360deg)' },
              }
            }
          },
        },
      }
    