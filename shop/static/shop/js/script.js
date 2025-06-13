document.addEventListener("DOMContentLoaded", function () {
  const header = document.getElementById("header");
  const heroSection = document.querySelector(".hero");
  let lastScrollY = window.scrollY;

  function toggleHeaderVisibility() {
    const heroHeight = heroSection.offsetHeight;

    if (window.scrollY > heroHeight) {
      // Estamos por debajo de la sección hero
      if (window.scrollY > lastScrollY) {
        // Scrolling down
        header.classList.add("hidden");
      } else {
        // Scrolling up
        header.classList.remove("hidden");
      }
    } else {
      header.classList.remove("hidden");
    }
    lastScrollY = window.scrollY;
  }

  // Ejecuta la función una vez al cargar para establecer el estado inicial
  toggleHeaderVisibility();

  // Añade el evento de scroll
  window.addEventListener("scroll", toggleHeaderVisibility);
});

document.addEventListener("DOMContentLoaded", function () {
  const track = document.querySelector(".carousel-track");
  const slides = Array.from(document.querySelectorAll(".carousel-slide"));
  const nextBtn = document.querySelector(".next-btn");
  const prevBtn = document.querySelector(".prev-btn");
  const indicators = document.querySelectorAll(".indicator");

  let currentIndex = 0;
  const slideCount = slides.length;

  function updateCarousel() {
    track.style.transform = `translateX(-${currentIndex * 100}%)`;

    // Actualiza indicadores
    indicators.forEach((indicator, index) => {
      indicator.classList.toggle("active", index === currentIndex);
    });

    // Actualiza slides
    slides.forEach((slide, index) => {
      slide.classList.toggle("active", index === currentIndex);
    });
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slideCount;
    updateCarousel();
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + slideCount) % slideCount;
    updateCarousel();
  }

  // Event listeners
  nextBtn.addEventListener("click", nextSlide);
  prevBtn.addEventListener("click", prevSlide);

  // Indicadores
  indicators.forEach((indicator, index) => {
    indicator.addEventListener("click", () => {
      currentIndex = index;
      updateCarousel();
    });
  });

  // Autoplay (opcional)
  setInterval(nextSlide, 10000);
});

// JavaScript para el menú hamburguesa
document.addEventListener("DOMContentLoaded", function () {
  const hamburgerBtn = document.querySelector(".hamburger-btn");
  const mainNav = document.querySelector(".main-nav");

  hamburgerBtn.addEventListener("click", function () {
    this.classList.toggle("active");
    mainNav.classList.toggle("active");

    // Bloquear el scroll cuando el menú está abierto
    if (mainNav.classList.contains("active")) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
  });

  // Cerrar el menú al hacer clic en un enlace (opcional)
  const navLinks = document.querySelectorAll(".main-nav a");
  navLinks.forEach((link) => {
    link.addEventListener("click", function () {
      hamburgerBtn.classList.remove("active");
      mainNav.classList.remove("active");
      document.body.style.overflow = "";
    });
  });
});
