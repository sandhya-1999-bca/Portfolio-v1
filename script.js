/**
 * script.js - Pure JavaScript for Portfolio Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Intersection Observer for Scroll Animations
    // Replaces Framer Motion 'whileInView' functionality.

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px', // Trigger slightly before it comes fully into view
        threshold: 0.1 // 10% of element visible
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add the class that triggers the CSS transition/animation
                entry.target.classList.add('is-visible');

                // Stop observing once animated (optional, matches standard Framer Motion behavior)
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Select all elements that need to animate on scroll
    const animatableElements = document.querySelectorAll('.animate-on-scroll');

    animatableElements.forEach(el => {
        scrollObserver.observe(el);
    });

    // 2. Smooth Scrolling for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
