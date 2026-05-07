import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {

  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {

    const handleScroll = () => {

      const hero =
        document.querySelector(".hero") ||
        document.querySelector(".hero-dibujo") ||
        document.querySelector(".noticia-hero") ||
        document.querySelector(".eventos-hero");

      const heroHeight = hero ? hero.offsetHeight : 400;

      setScrolled(window.scrollY > heroHeight - 140);
    };

    window.addEventListener("scroll", handleScroll);

    return () =>
      window.removeEventListener("scroll", handleScroll);

  }, []);

  return (

    <header className={`navbar ${scrolled ? "scrolled" : ""}`}>

      {/* LOGO */}
      <div className="logo">

        <img
          src="/img/Logo-principal.png"
          alt="Logo"
        />

      </div>

      {/* LINKS */}
      <nav className="nav-links">

        <Link to="/">
          Inicio
        </Link>

        <Link to="/noticias">
          Noticias
        </Link>

        <Link to="/eventos">
          Eventos
        </Link>

        {/* AFUERA DEL DROPDOWN */}
        <Link to="/autoridades">
          Autoridades
        </Link>

        <Link to="/contactanos">
          Contáctanos
        </Link>

        {/* DROPDOWN */}
        <div className="dropdown">

          <span className="dropdown-title">
            Sobre Nosotros ▾
          </span>

          <div className="dropdown-menu">

            <Link to="/nosotros/historia">
              Nuestra historia
            </Link>

            <Link to="/nosotros/conocenos">
              Conócenos
            </Link>

          </div>

        </div>

      </nav>

      {/* BOTÓN */}
      <button className="btn-login">
        Ingresar
      </button>

    </header>

  );
}

export default Navbar;