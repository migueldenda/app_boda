        // Fecha objetivo: 6 de junio de 2026 a las 00:00:00
        const fechaBoda = new Date('2026-06-06T00:00:00').getTime();

        function actualizarCuentaAtras() {
            const ahora = new Date().getTime();
            const diferencia = fechaBoda - ahora;

            // Calcular días, horas, minutos y segundos
            const dias = Math.floor(diferencia / (1000 * 60 * 60 * 24));
            const horas = Math.floor((diferencia % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutos = Math.floor((diferencia % (1000 * 60 * 60)) / (1000 * 60));
            const segundos = Math.floor((diferencia % (1000 * 60)) / 1000);

            // Crear el HTML de la cuenta atrás
            const cuentaAtrasHTML = `
                <div class="tiempo-bloque" id="bloque-dias">
                    <span class="tiempo-numero">${dias}</span>
                    <span class="tiempo-label">Días</span>
                </div>
                <div class="tiempo-bloque" id="bloque-horas">
                    <span class="tiempo-numero">${horas.toString().padStart(2, '0')}</span>
                    <span class="tiempo-label">Horas</span>
                </div>
                <div class="tiempo-bloque" id="bloque-minutos">
                    <span class="tiempo-numero">${minutos.toString().padStart(2, '0')}</span>
                    <span class="tiempo-label">Minutos</span>
                </div>
                <div class="tiempo-bloque" id="bloque-segundos">
                    <span class="tiempo-numero">${segundos.toString().padStart(2, '0')}</span>
                    <span class="tiempo-label">Segundos</span>
                </div>
            `;

            document.getElementById('cuenta-atras').innerHTML = cuentaAtrasHTML;

            // Efecto de pulso en los segundos cada vez que cambian
            const bloqueSegundos = document.getElementById('bloque-segundos');
            bloqueSegundos.classList.add('pulse');
            setTimeout(() => bloqueSegundos.classList.remove('pulse'), 500);

            // Si la fecha ya pasó
            if (diferencia < 0) {
                document.getElementById('cuenta-atras').innerHTML = `
                    <div style="grid-column: 1 / -1; text-align: center; font-size: 2rem; color: #8b7355;">
                        ¡Es hoy! 💒
                    </div>
                `;
                clearInterval(intervalo);
            }
        }

        // Actualizar cada segundo
        actualizarCuentaAtras();
        const intervalo = setInterval(actualizarCuentaAtras, 1000);