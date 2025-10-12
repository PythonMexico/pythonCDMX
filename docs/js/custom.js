// Python CDMX Custom JavaScript
document.addEventListener('DOMContentLoaded', function() {

    // Lazy loading para imágenes
    const lazyImages = document.querySelectorAll('.lazy-image');

    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    lazyImages.forEach(img => {
        imageObserver.observe(img);
    });

    // Animaciones suaves para las tarjetas de voluntarios
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const cardObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    const volunteerCards = document.querySelectorAll('.volunteer-card');
    volunteerCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        cardObserver.observe(card);
    });

    // Mejoras de navegación
    const navLinks = document.querySelectorAll('.md-nav__link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Añadir efecto de ripple
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            this.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Scroll suave para enlaces internos
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    internalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Mejoras de tablas
    const tables = document.querySelectorAll('.md-typeset table');
    tables.forEach(table => {
        // Añadir hover effects
        const rows = table.querySelectorAll('tr');
        rows.forEach(row => {
            row.addEventListener('mouseenter', function() {
                this.style.backgroundColor = 'rgba(38, 159, 70, 0.05)';
            });

            row.addEventListener('mouseleave', function() {
                this.style.backgroundColor = '';
            });
        });

        // Hacer tablas responsivas
        const wrapper = document.createElement('div');
        wrapper.style.overflowX = 'auto';
        wrapper.style.borderRadius = '12px';
        wrapper.style.boxShadow = '0 2px 8px rgba(0,0,0,0.1)';

        table.parentNode.insertBefore(wrapper, table);
        wrapper.appendChild(table);
    });

    // Botones de acción mejorados
    const actionButtons = document.querySelectorAll('.btn-action');
    actionButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Efecto de click
            const ripple = document.createElement('span');
            ripple.classList.add('button-ripple');
            this.appendChild(ripple);

            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });

    // Optimización de rendimiento en resize
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            // Recalcular posiciones después del resize
            cardObserver.disconnect();
            volunteerCards.forEach(card => {
                cardObserver.observe(card);
            });
        }, 250);
    });

    // Mejoras de accesibilidad
    const focusableElements = document.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            focusableElements.forEach(element => {
                element.addEventListener('focus', function() {
                    this.style.outline = '2px solid var(--python-green)';
                    this.style.outlineOffset = '2px';
                });

                element.addEventListener('blur', function() {
                    this.style.outline = '';
                    this.style.outlineOffset = '';
                });
            });
        }
    });

    // Mejoras de dark mode
    const darkModeToggle = document.querySelector('[data-md-color-scheme]');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', function() {
            // Añadir transición suave para el cambio de tema
            document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
            setTimeout(() => {
                document.body.style.transition = '';
            }, 300);
        });
    }

    // Animar elementos de la página al cargar
    window.addEventListener('load', function() {
        const animatedElements = document.querySelectorAll('.hero-section, .stats-grid, .features-grid');
        animatedElements.forEach((element, index) => {
            setTimeout(() => {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }, index * 200);
        });
    });

    // Mejoras de UX para móviles
    if (window.innerWidth <= 768) {
        // Optimizar navegación móvil
        const mobileNav = document.querySelector('.md-nav');
        if (mobileNav) {
            mobileNav.addEventListener('touchstart', function() {
                this.style.transform = 'scale(0.98)';
            });

            mobileNav.addEventListener('touchend', function() {
                this.style.transform = '';
            });
        }

        // Mejorar scroll en móviles
        let isScrolling;
        window.addEventListener('scroll', function() {
            window.clearTimeout(isScrolling);
            isScrolling = setTimeout(function() {
                // Pausar animaciones durante scroll
                document.body.classList.add('scrolling');
                setTimeout(() => {
                    document.body.classList.remove('scrolling');
                }, 100);
            }, 66);
        });
    }

    console.log('Python CDMX Custom JavaScript loaded successfully!');
});

// Estilos CSS para los efectos de JavaScript
const additionalStyles = `
    .button-ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }

    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }

    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(38, 159, 70, 0.2);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }

    .scrolling * {
        animation-play-state: paused !important;
    }

    @media (max-width: 768px) {
        .button-ripple {
            display: none;
        }
    }
`;

// Inyectar estilos adicionales
const styleSheet = document.createElement('style');
styleSheet.textContent = additionalStyles;
document.head.appendChild(styleSheet);
