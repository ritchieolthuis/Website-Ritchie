
        window.openExpertiseOverlay = function() {
             const overlay = document.getElementById('expertise-overlay');
             if(overlay) {
                 overlay.classList.remove('hidden');
                 document.body.style.overflow = 'hidden';
             }
        };
        window.closeExpertiseOverlay = function() {
             const overlay = document.getElementById('expertise-overlay');
             if(overlay) {
                 overlay.classList.add('hidden');
                 document.body.style.overflow = 'auto';
             }
        };

        window.openProjectsModal = function() {
             const modal = document.getElementById('projects-modal-unique');
             if(modal) {
                 modal.classList.remove('hidden');
                 document.body.style.overflow = 'hidden';
             }
        };
        window.closeProjectsModal = function() {
             const modal = document.getElementById('projects-modal-unique');
             if(modal) {
                 modal.classList.add('hidden');
                 document.body.style.overflow = 'auto';
             }
        };

        window.openServicesModal = function() {
             const modal = document.getElementById('services-modal');
             if(modal) {
                 modal.classList.remove('hidden');
                 document.body.style.overflow = 'hidden';
             }
        };
        window.closeServicesModal = function() {
             const modal = document.getElementById('services-modal');
             if(modal) {
                 modal.classList.add('hidden');
                 document.body.style.overflow = 'auto';
             }
        };

        window.openContactModal = function() {
             const modal = document.getElementById('contact-modal');
             if(modal) {
                 modal.classList.remove('hidden');
                 document.body.style.overflow = 'hidden';
             }
        };
        window.closeContactModal = function() {
             const modal = document.getElementById('contact-modal');
             if(modal) {
                 modal.classList.add('hidden');
                 document.body.style.overflow = 'auto';
             }
        };
        
        window.openCallModal = function() {
             const modal = document.getElementById('call-modal');
             if(modal) {
                 modal.classList.remove('hidden');
                 document.body.style.overflow = 'hidden';
             }
        };
        window.closeCallModal = function() {
             const modal = document.getElementById('call-modal');
             if(modal) {
                 modal.classList.add('hidden');
                 document.body.style.overflow = 'auto';
             }
        };

        window.openCVModal = function() {
             const modal = document.getElementById('cv-modal');
             if(modal) {
                 modal.classList.remove('hidden');
                 document.body.style.overflow = 'hidden';
             }
        };
        window.closeCVModal = function() {
             const modal = document.getElementById('cv-modal');
             if(modal) {
                 modal.classList.add('hidden');
                 document.body.style.overflow = 'auto';
             }
        };
    