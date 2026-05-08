// App.js

import React, { useState, useEffect } from "react";

import {
  BrowserRouter,
  Routes,
  Route,
  Link,
  useLocation,
} from "react-router-dom";

import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

import Noticias from "./pages/Noticias/Noticias";
import DetalleNoticia from "./pages/Noticias/DetalleNoticia";

import Eventos from "./pages/Eventos/Eventos";
import DetalleEvento from "./pages/Eventos/DetalleEvento";

import NuestraHistoria from "./pages/Nosotros/NuestraHistoria";
import Conocenos from "./pages/Nosotros/Conocenos";

import Autoridades from "./components/Autoridades/Autoridades";
import Contacto from "./components/Contacto/Contacto";

import LibroReclamaciones from "./components/LibroReclamaciones/LibroReclamaciones";

import "./App.css";

/* SCROLL ARRIBA AUTOMÁTICO */
function ScrollToTop() {

  const { pathname } = useLocation();

  useEffect(() => {

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });

  }, [pathname]);

  return null;
}

/* HOME */
function Home() {

  const [faqAbierta, setFaqAbierta] = useState(null);

  const preguntas = [
    {
      pregunta: "¿Qué información ofrece la plataforma?",
      respuesta:
        "La plataforma brinda acceso a noticias, eventos, comunicados y contenido institucional relacionado con la Comunidad Campesina Zapotal.",
    },
    {
      pregunta: "¿Para quién está dirigida?",
      respuesta:
        "Está dirigida a comuneros, autoridades, visitantes e integrantes interesados en conocer las actividades y organización de la comunidad.",
    },
    {
      pregunta: "¿Cómo puedo visualizar las actividades y eventos?",
      respuesta:
        "Puedes ingresar a la sección Eventos para consultar las actividades programadas, reuniones y fechas importantes.",
    },
  ];

  return (
    <main className="main-container">

      {/* HERO */}
      <section className="hero-dibujo">

        <div className="hero-reveal"></div>

        <div className="hero-overlay"></div>

        <div className="hero-content">

          <span className="hero-etiqueta">
            Comunidad • Cultura • Organización
          </span>

          <h1>
            Comunidad <br />
            Campesina <br />
            Zapotal
          </h1>

          <p>
            Un espacio digital moderno creado para informar,
            conectar y fortalecer la identidad de nuestra
            comunidad mediante noticias, eventos y contenido
            relevante para todos los comuneros.
          </p>

          <div className="hero-botones">

            <Link
              to="/nosotros/conocenos"
              className="btn-principal"
            >
              Conócenos
            </Link>

            <Link
              to="/noticias"
              className="btn-linea"
            >
              Ver noticias
            </Link>

          </div>

        </div>

      </section>

      {/* INTRO */}
      <section className="intro-section">

        <div className="intro-texto">

          <span>Nuestra plataforma</span>

          <h2>
            Información clara para una comunidad más conectada
          </h2>

          <p>
            Este portal digital permite compartir noticias,
            eventos y contenido relevante de manera organizada,
            moderna y accesible.
          </p>

        </div>

        <div className="intro-panel">

          <div className="panel-item">
            <strong>01</strong>
            <p>Noticias actualizadas</p>
          </div>

          <div className="panel-item">
            <strong>02</strong>
            <p>Eventos comunitarios</p>
          </div>

          <div className="panel-item">
            <strong>03</strong>
            <p>Historia e identidad</p>
          </div>

        </div>

      </section>

      {/* CARDS */}
      <section className="cards-section">

        <h2>Explora nuestro contenido</h2>

        <div className="cards">

          <div className="card">

            <h3>Noticias</h3>

            <p>
              Consulta información relevante y comunicados importantes.
            </p>

            <Link to="/noticias">
              Ingresar
            </Link>

          </div>

          <div className="card">

            <h3>Eventos</h3>

            <p>
              Revisa actividades, reuniones y fechas importantes.
            </p>

            <Link to="/eventos">
              Ingresar
            </Link>

          </div>

          <div className="card">

            <h3>Nosotros</h3>

            <p>
              Conoce nuestra historia, valores y organización comunal.
            </p>

            <Link to="/nosotros/historia">
              Ingresar
            </Link>

          </div>

        </div>

      </section>

      {/* FAQ */}
      <section className="faq-section">

        <div className="faq-header">

          <span className="faq-subtitle">
            Centro de información
          </span>

          <h2>Preguntas Frecuentes</h2>

          <p>
            Resolvemos las principales dudas relacionadas
            con la plataforma digital de la Comunidad
            Campesina Zapotal.
          </p>

        </div>

        <div className="faq-list">

          {preguntas.map((item, index) => (

            <div
              className={`faq-item ${
                faqAbierta === index ? "faq-activa" : ""
              }`}
              key={index}
            >

              <button
                onClick={() =>
                  setFaqAbierta(
                    faqAbierta === index ? null : index
                  )
                }
              >

                <span>{item.pregunta}</span>

                <div className="faq-icono">

                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="22"
                    height="22"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2.2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <polyline points="6 9 12 15 18 9"></polyline>
                  </svg>

                </div>

              </button>

              <div className="faq-contenido">
                <p>{item.respuesta}</p>
              </div>

            </div>

          ))}

        </div>

      </section>

    </main>
  );
}

/* LAYOUT */
function Layout() {

  const location = useLocation();

  const ocultarNavbar =
    location.pathname.startsWith("/noticias/") ||
    location.pathname.startsWith("/eventos/") ||
    location.pathname.startsWith("/libro-reclamaciones");

  return (
    <>

      <ScrollToTop />

      {!ocultarNavbar && <Navbar />}

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/noticias"
          element={<Noticias />}
        />

        <Route
          path="/noticias/:id"
          element={<DetalleNoticia />}
        />

        <Route
          path="/eventos"
          element={<Eventos />}
        />

        <Route
          path="/eventos/:id"
          element={<DetalleEvento />}
        />

        <Route
          path="/nosotros/historia"
          element={<NuestraHistoria />}
        />

        <Route
          path="/nosotros/conocenos"
          element={<Conocenos />}
        />

        <Route
          path="/autoridades"
          element={<Autoridades />}
        />

        <Route
          path="/contactanos"
          element={<Contacto />}
        />

        <Route
          path="/libro-reclamaciones"
          element={<LibroReclamaciones />}
        />

      </Routes>

      {!ocultarNavbar && <Footer />}

    </>
  );
}

/* APP */
function App() {

  return (

    <BrowserRouter>

      <Layout />

    </BrowserRouter>

  );
}

export default App;