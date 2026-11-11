/* ================================================
   KS ON THE KEYS — Interactive JS
   ================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ── Menu Tabs ──────────────────────────────────
  const tabs = document.querySelectorAll('.menu-tab');
  const panels = document.querySelectorAll('.menu-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.tab;

      tabs.forEach(t => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      panels.forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      const targetPanel = document.getElementById('panel-' + target);
      if (targetPanel) {
        targetPanel.classList.add('active');
        // Animate cards in
        targetPanel.querySelectorAll('.menu-card').forEach((card, i) => {
          card.style.opacity = '0';
          card.style.transform = 'translateY(16px)';
          setTimeout(() => {
            card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, i * 40);
        });
      }
    });
  });

  // ── FAQ Accordion ──────────────────────────────
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');

    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');

      // Close all
      faqItems.forEach(i => {
        i.classList.remove('open');
        i.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
      });

      // Toggle clicked
      if (!isOpen) {
        item.classList.add('open');
        question.setAttribute('aria-expanded', 'true');
      }
    });

    // Keyboard support
    question.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        question.click();
      }
    });
  });

  // ── Mobile Menu ────────────────────────────────
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileClose = document.getElementById('mobile-close');

  function openMenu() {
    mobileMenu.classList.add('open');
    hamburger.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    mobileMenu.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (hamburger) hamburger.addEventListener('click', openMenu);
  if (mobileClose) mobileClose.addEventListener('click', closeMenu);

  // Close mobile menu when a link is clicked
  document.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  // Close on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu.classList.contains('open')) {
      closeMenu();
    }
  });

  // ── Scroll Reveal ──────────────────────────────
  const fadeEls = document.querySelectorAll('.fade-in');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, 80);
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  fadeEls.forEach(el => observer.observe(el));

  // ── Navbar Scroll Behavior ─────────────────────
  const navbar = document.getElementById('navbar');
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
  }, { passive: true });

  // ── Smooth Scroll for anchor links ────────────
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 80; // navbar height
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ── Current open status indicator ─────────────
  function updateOpenStatus() {
    const now = new Date();
    const formatter = new Intl.DateTimeFormat('en-US', {
      timeZone: 'America/Toronto',
      weekday: 'short',
      hour: 'numeric',
      minute: 'numeric',
      hour12: false
    });
    const parts = formatter.formatToParts(now);
    const weekdayStr = parts.find(p => p.type === 'weekday')?.value || 'Sun';
    let hour = parseInt(parts.find(p => p.type === 'hour')?.value || '0', 10);
    if (hour === 24) hour = 0;
    const minute = parseInt(parts.find(p => p.type === 'minute')?.value || '0', 10);
    const timeNum = hour * 100 + minute;

    const dayMap = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    const day = dayMap[weekdayStr] ?? now.getDay();

    let isOpen = false;

    if (day === 1) { // Monday
      isOpen = false;
    } else if (day === 2 || day === 3) { // Tue/Wed: 11am–8pm
      isOpen = timeNum >= 1100 && timeNum < 2000;
    } else if (day === 4 || day === 5) { // Thu/Fri: 11am–10pm
      isOpen = timeNum >= 1100 && timeNum < 2200;
    } else if (day === 6) { // Sat: 10am–10pm
      isOpen = timeNum >= 1000 && timeNum < 2200;
    } else if (day === 0) { // Sun: 9am–8pm
      isOpen = timeNum >= 900 && timeNum < 2000;
    }

    // Add status to top bar
    const topBar = document.querySelector('.top-bar-inner');
    if (topBar && !topBar.querySelector('.open-status-badge')) {
      const statusBadge = document.createElement('span');
      statusBadge.className = 'open-status-badge';
      statusBadge.style.cssText = `
        background: ${isOpen ? 'rgba(76,175,80,0.25)' : 'rgba(244,67,54,0.25)'};
        color: ${isOpen ? '#81C784' : '#FF8A80'};
        border: 1px solid ${isOpen ? 'rgba(76,175,80,0.5)' : 'rgba(244,67,54,0.5)'};
        border-radius: 20px;
        padding: 2px 10px;
        font-size: 0.72rem;
        font-weight: 600;
        white-space: nowrap;
      `;
      statusBadge.textContent = isOpen ? '● Open Now' : '● Closed';
      topBar.prepend(statusBadge);
    }

    // Dynamically adjust navbar top offset so it never overlaps the top-bar
    function syncNavbarOffset() {
      const topBarEl = document.querySelector('.top-bar');
      const navEl = document.getElementById('navbar');
      if (topBarEl && navEl) {
        if (window.pageYOffset > 50) {
          navEl.style.top = '0px';
        } else {
          navEl.style.top = topBarEl.offsetHeight + 'px';
        }
      }
    }
    syncNavbarOffset();
    window.addEventListener('resize', syncNavbarOffset);
    window.addEventListener('scroll', syncNavbarOffset, { passive: true });
  }

  updateOpenStatus();

  // ——— Hero Video Mobile Optimization (<768px) ———
  const heroVideo = document.getElementById('hero-video');
  if (heroVideo && window.innerWidth < 768) {
    heroVideo.pause();
    heroVideo.removeAttribute('autoplay');
    heroVideo.querySelectorAll('source').forEach(s => s.remove());
    heroVideo.load();
  }

  // ——— Lightbox Modal Logic ———
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxImg = document.getElementById('lightboxImg');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxPrev = document.getElementById('lightboxPrev');
  const lightboxNext = document.getElementById('lightboxNext');

  let currentGallery = [];
  let currentIndex = 0;

  if (lightboxModal && lightboxImg && lightboxClose) {
    const lightboxTriggers = document.querySelectorAll('.lightbox-trigger');
    
    lightboxTriggers.forEach(trigger => {
      trigger.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Determine the gallery context (the container holding these images)
        const parent = this.closest('.gallery-grid, .gallery-section, .space-slideshow, .container');
        if (parent) {
          currentGallery = Array.from(parent.querySelectorAll('.lightbox-trigger'));
          currentIndex = currentGallery.indexOf(this);
        } else {
          currentGallery = [this];
          currentIndex = 0;
        }
        
        updateLightboxImage();
        lightboxModal.classList.add('show');
        document.body.style.overflow = 'hidden'; 
      });
    });

    function updateLightboxImage() {
      const target = currentGallery[currentIndex];
      if (!target) return;
      const src = target.getAttribute('src') || target.getAttribute('data-src');
      if (src) {
        lightboxImg.style.opacity = '0';
        setTimeout(() => {
          lightboxImg.src = src;
          lightboxImg.style.opacity = '1';
        }, 150);
      }
      
      // Hide arrows if only one image
      if (lightboxPrev && lightboxNext) {
        const display = currentGallery.length > 1 ? 'flex' : 'none';
        lightboxPrev.style.display = display;
        lightboxNext.style.display = display;
      }
    }

    function showNext() {
      if (currentGallery.length <= 1) return;
      currentIndex = (currentIndex + 1) % currentGallery.length;
      updateLightboxImage();
    }

    function showPrev() {
      if (currentGallery.length <= 1) return;
      currentIndex = (currentIndex - 1 + currentGallery.length) % currentGallery.length;
      updateLightboxImage();
    }

    if (lightboxNext) lightboxNext.addEventListener('click', (e) => { e.stopPropagation(); showNext(); });
    if (lightboxPrev) lightboxPrev.addEventListener('click', (e) => { e.stopPropagation(); showPrev(); });

    // Close on click close button
    lightboxClose.addEventListener('click', () => {
      lightboxModal.classList.remove('show');
      document.body.style.overflow = '';
      setTimeout(() => lightboxImg.src = '', 300);
    });

    // Close on click outside image
    lightboxModal.addEventListener('click', (e) => {
      if (e.target === lightboxModal) {
        lightboxModal.classList.remove('remove');
        lightboxModal.classList.remove('show');
        document.body.style.overflow = '';
        setTimeout(() => lightboxImg.src = '', 300);
      }
    });

    // Keyboard support
    document.addEventListener('keydown', (e) => {
      if (!lightboxModal.classList.contains('show')) return;
      
      if (e.key === 'Escape') {
        lightboxModal.classList.remove('show');
        document.body.style.overflow = '';
        setTimeout(() => lightboxImg.src = '', 300);
      } else if (e.key === 'ArrowRight') {
        showNext();
      } else if (e.key === 'ArrowLeft') {
        showPrev();
      }
    });
  }

});
