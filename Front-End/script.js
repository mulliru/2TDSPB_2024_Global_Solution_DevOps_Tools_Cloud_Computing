document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('add-point-form');
    const pointsList = document.getElementById('points-list');

    // Função para buscar todos os pontos de abastecimento
    function fetchPoints() {
        fetch('http://localhost:5000/points')
            .then(response => response.json())
            .then(data => {
                pointsList.innerHTML = '';
                data.forEach(point => {
                    const li = document.createElement('li');
                    li.textContent = `${point.nome} - ${point.rua}, ${point.cidade}, ${point.estado} (Tipo: ${point.tipo_carregador}, Capacidade: ${point.capacidade} kW)`;
                    pointsList.appendChild(li);
                });
            })
            .catch(error => console.error('Erro ao buscar pontos:', error));
    }

    // Buscar todos os pontos quando a página carregar
    fetchPoints();

    // Evento de submissão do formulário
    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = {
            nome: form.nome.value,
            rua: form.rua.value,
            cidade: form.cidade.value,
            estado: form.estado.value,
            tipo_carregador: form.tipo_carregador.value,
            capacidade: form.capacidade.value
        };

        fetch('http://localhost:5000/points', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Ponto adicionado:', data);
            fetchPoints(); // Atualiza a lista de pontos
            form.reset();
        })
        .catch(error => console.error('Erro ao adicionar ponto:', error));
    });
});
