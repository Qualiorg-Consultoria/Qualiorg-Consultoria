function toggleMenu() {
  document.querySelector('nav').classList.toggle('open');
}

function enviarFormulario(e) {
  e.preventDefault();
  const feedback = document.getElementById('form-feedback');
  feedback.textContent = '✓ Mensagem enviada! Fernando entrará em contato em breve.';
  e.target.reset();
  setTimeout(() => { feedback.textContent = ''; }, 6000);
}

// Highlight nav link on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 80) current = s.id;
  });
  navLinks.forEach(a => {
    a.classList.remove('active');
    if (a.getAttribute('href') === '#' + current) a.classList.add('active');
  });
});
