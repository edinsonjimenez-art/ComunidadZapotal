import React from "react";
import "./Footer.css";
import { FaMapMarkerAlt, FaEnvelope, FaPhone } from "react-icons/fa";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">

        {/* INFO */}
        <div className="footer-section">
          <h2>Comunidad Zapotal</h2>
          <p>
            Plataforma digital para mantener informados a los comuneros
            sobre noticias, eventos y actividades de la comunidad.
          </p>
        </div>

        {/* LINKS */}
        <div className="footer-section">
          <h3>Enlaces</h3>
          <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/noticias">Noticias</a></li>
            <li><a href="/eventos">Eventos</a></li>
            <li><a href="/nosotros">Sobre Nosotros</a></li>
          </ul>
        </div>

        {/* CONTACTO */}
        <div className="footer-section">
          <h3>Contacto</h3>

          <p><FaMapMarkerAlt className="icon" /> Cajamarca, Perú</p>
          <p><FaEnvelope className="icon" /> comunidad@zapotal.com</p>
          <p><FaPhone className="icon" /> +51 921456783</p>

        </div>

      </div>

      <div className="footer-bottom">
        <p>© 2026 Comunidad Campesina Zapotal</p>
      </div>
    </footer>
  );
}

export default Footer;