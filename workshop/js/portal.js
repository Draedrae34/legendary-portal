// Portal Animation System
class PortalAnimation {
    constructor() {
        this.stars = [];
        this.portalActive = false;
        this.animationId = null;
        this.init();
    }

    init() {
        this.createGalaxy();
        this.setupEventListeners();
    }

    createGalaxy() {
        const galaxyContainer = document.querySelector('.galaxy-container');
        const starCount = 1000;

        for (let i = 0; i < starCount; i++) {
            const star = document.createElement('div');
            star.className = 'stars';
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.animationDelay = `${Math.random() * 5}s`;
            star.style.width = `${Math.random() * 2}px`;
            star.style.height = `${Math.random() * 2}px`;
            star.style.boxShadow = `0 0 ${Math.random() * 5}px #fff`;
            galaxyContainer.appendChild(star);
            this.stars.push(star);
        }
    }

    setupEventListeners() {
        document.getElementById('activate').addEventListener('click', () => this.activatePortal());
        document.getElementById('deactivate').addEventListener('click', () => this.deactivatePortal());
    }

    activatePortal() {
        if (!this.portalActive) {
            this.portalActive = true;
            this.animatePortal(true);
        }
    }

    deactivatePortal() {
        if (this.portalActive) {
            this.portalActive = false;
            this.animatePortal(false);
        }
    }

    animatePortal(activate) {
        const portal = document.querySelector('.portal');
        if (activate) {
            portal.style.transform = 'scale(1.2)';
            portal.style.boxShadow = '0 0 100px rgba(138, 43, 226, 0.8)';
            this.startFractalAnimation();
        } else {
            portal.style.transform = 'scale(1)';
            portal.style.boxShadow = '0 0 50px rgba(138, 43, 226, 0.5)';
            this.stopFractalAnimation();
        }
    }

    startFractalAnimation() {
        this.animationId = requestAnimationFrame(this.fractalAnimation.bind(this));
    }

    stopFractalAnimation() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
    }

    fractalAnimation() {
        // Advanced fractal animation logic would go here
        // For now, we'll just keep the animation running
        this.animationId = requestAnimationFrame(this.fractalAnimation.bind(this));
    }
}

// Initialize the portal animation when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PortalAnimation();
});