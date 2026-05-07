import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "./Eventos.css";

function Eventos() {
  const [eventos, setEventos] = useState([]);
  const [mensaje, setMensaje] = useState("Cargando eventos...");

  const [busqueda, setBusqueda] = useState("");
  const [comunidad, setComunidad] = useState("");

  const [busquedaAplicada, setBusquedaAplicada] = useState("");
  const [comunidadAplicada, setComunidadAplicada] = useState("");

  const [mostrarSugerencias, setMostrarSugerencias] = useState(false);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/eventos/")
      .then((res) => {
        const datos = Array.isArray(res.data)
          ? res.data
          : res.data.results || [];

        setEventos(datos);
        setMensaje("");
      })
      .catch((error) => {
        console.log("ERROR API:", error);
        setMensaje("Error al cargar eventos.");
      });
  }, []);

  const sugerencias = eventos.filter((evento) =>
    evento.titulo?.toLowerCase().includes(busqueda.toLowerCase())
  );

  const buscarEventos = () => {
    setBusquedaAplicada(busqueda);
    setComunidadAplicada(comunidad);
    setMostrarSugerencias(false);
  };

  const eventosFiltrados = eventos.filter((evento) => {
    const textoBusqueda = busquedaAplicada.toLowerCase();
    const textoComunidad = comunidadAplicada.toLowerCase();

    const coincideBusqueda =
      textoBusqueda === "" ||
      evento.titulo?.toLowerCase().includes(textoBusqueda);

    const coincideComunidad =
      textoComunidad === "" ||
      "comunidad zapotal".includes(textoComunidad) ||
      evento.titulo?.toLowerCase().includes(textoComunidad) ||
      evento.descripcion?.toLowerCase().includes(textoComunidad);

    return coincideBusqueda && coincideComunidad;
  });

  const seleccionarEvento = (titulo) => {
    setBusqueda(titulo);
    setMostrarSugerencias(false);
  };

  const limpiarFiltros = () => {
    setBusqueda("");
    setComunidad("");
    setBusquedaAplicada("");
    setComunidadAplicada("");
    setMostrarSugerencias(false);
  };

  return (
    <main className="eventos-page">
      <section className="eventos-hero">
        <div className="eventos-hero-content">
          <h1>Encuentra eventos y actividades de la comunidad</h1>

          <div className="eventos-buscador">
            <div className="autocomplete">
              <input
                type="text"
                placeholder="¿Qué evento estás buscando?"
                value={busqueda}
                onChange={(e) => {
                  setBusqueda(e.target.value);
                  setMostrarSugerencias(true);
                }}
                onFocus={() => setMostrarSugerencias(true)}
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    buscarEventos();
                  }
                }}
              />

              {mostrarSugerencias && sugerencias.length > 0 && (
                <ul className="sugerencias-lista">
                  {sugerencias.map((evento) => (
                    <li
                      key={evento.id}
                      onClick={() => seleccionarEvento(evento.titulo)}
                    >
                      {evento.titulo}
                    </li>
                  ))}
                </ul>
              )}
            </div>

            <input
              type="text"
              placeholder="Comunidad Zapotal"
              value={comunidad}
              onChange={(e) => setComunidad(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  buscarEventos();
                }
              }}
            />

            <button type="button" onClick={buscarEventos}>
              Buscar
            </button>
          </div>

          {(busquedaAplicada || comunidadAplicada) && (
            <button className="btn-limpiar" onClick={limpiarFiltros}>
              Limpiar filtros
            </button>
          )}
        </div>
      </section>

      <div className="eventos-header">
        <h1>Eventos de la Comunidad</h1>

        {(busquedaAplicada || comunidadAplicada) && (
          <p>
            Mostrando resultados para:{" "}
            <strong>{busquedaAplicada || "Todos los eventos"}</strong>
          </p>
        )}

        {!busquedaAplicada && !comunidadAplicada && (
          <p>
            Conoce las actividades, reuniones y jornadas organizadas para
            nuestros comuneros.
          </p>
        )}
      </div>

      {mensaje && <p className="mensaje">{mensaje}</p>}

      {!mensaje && eventosFiltrados.length === 0 && (
        <p className="mensaje">No se encontraron eventos.</p>
      )}

      <div className="eventos-grid">
        {eventosFiltrados.map((evento) => {
          const mediaPrincipal = evento.multimedia?.[0];

          return (
            <article className="evento-card" key={evento.id}>
              {mediaPrincipal && (
                <div className="evento-media">
                  {mediaPrincipal.tipo === "IMAGEN" && (
                    <img
                      src={mediaPrincipal.archivo_url}
                      alt={evento.titulo}
                      className="evento-img"
                    />
                  )}

                  {mediaPrincipal.tipo === "VIDEO" && (
                    <video className="evento-video" controls>
                      <source
                        src={mediaPrincipal.archivo_url}
                        type="video/mp4"
                      />
                      Tu navegador no soporta video.
                    </video>
                  )}
                </div>
              )}

              <div className="evento-content">
                <span className="evento-fecha">
                  {new Date(evento.fecha_evento).toLocaleDateString("es-PE", {
                    day: "2-digit",
                    month: "long",
                    year: "numeric",
                  })}
                </span>

                <h2>{evento.titulo}</h2>

                <p>
                  {evento.descripcion?.length > 120
                    ? evento.descripcion.substring(0, 120) + "..."
                    : evento.descripcion}
                </p>

                <Link to={`/eventos/${evento.id}`} className="btn-evento">
                  LEER MÁS →
                </Link>
              </div>
            </article>
          );
        })}
      </div>
    </main>
  );
}

export default Eventos;