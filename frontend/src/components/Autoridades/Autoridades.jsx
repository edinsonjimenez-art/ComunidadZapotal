import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Autoridades.css";

function Autoridades() {

  const [autoridades, setAutoridades] = useState([]);

  useEffect(() => {

    axios
      .get("http://127.0.0.1:8000/api/autoridades/")

      .then((res) => {

        setAutoridades(res.data);

      })

      .catch((err) => {

        console.log(err);

      });

  }, []);

  return (

    <section className="autoridades-section">

      <div className="autoridades-header">
        <h2>
          Líderes de la Comunidad Campesina Zapotal
        </h2>

        <p>
          Autoridades comprometidas con el desarrollo,
          organización y bienestar de nuestra comunidad.
        </p>

      </div>

      <div className="autoridades-grid">

        {autoridades.map((autoridad) => (

          <div
            className="autoridad-card"
            key={autoridad.id}
          >

            <div className="autoridad-imagen">

              <img
                src={autoridad.foto_url}
                alt={autoridad.nombres}
              />

            </div>

            <div className="autoridad-info">

              <h3>
                {autoridad.nombres} {autoridad.apellidos}
              </h3>

              <h4>
                {autoridad.cargo}
              </h4>

              <p>
                {autoridad.descripcion}
              </p>

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}

export default Autoridades;