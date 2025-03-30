---
layout: page_larga  
title: Jornal eVTOL - 1ª edição
subtitle: Notícias sobre nosso progresso 
cover-img: jornal_evtol/1a_edicao/assets/img/ita_e_usp.png 
thumbnail-img: /assets/img/posts/cbr_2023.jpg  
share-img: /assets/img/posts/cbr_2023.jpg  
tags: [jornal eVTOL, drones, 2025]
---

<style>
    .mexendo_drone {
        display: flex; /* Define um layout flexível para colocar os itens lado a lado */
        justify-content: space-between; /* Adiciona espaço entre os itens */
        align-items: flex-end; /* Alinha os itens pela parte inferior */
        gap: 50px; /* Espaçamento entre os itens */
    }

    .mexendo_drone img {
        max-width: 48%; /* Limita a largura de cada imagem a 48% do contêiner */
        height: auto; /* Mantém a proporção da imagem */
        object-fit: cover; /* Garante que a imagem seja cortada, se necessário, sem distorção */
        border-radius: 5px; /* (Opcional) Adiciona bordas arredondadas às imagens */
    }
    .imagem_centrada {
        display: flex;
        justify-content: center; /* Centraliza horizontalmente */
        align-items: center; /* Centraliza verticalmente (se necessário) */
        margin-top: 20px; /* Adiciona um espaçamento acima da imagem */
    }

    .imagem_centrada img {
        max-width: 100%; /* Garante que a imagem não ultrapasse o contêiner */
        height: auto; /* Mantém a proporção da imagem */
    }
    .imagem_lado_a_lado {
        display: flex; /* Coloca as imagens lado a lado */
        justify-content: center; /* Centraliza as imagens horizontalmente */
        align-items: center; /* Alinha as imagens pela altura */
        gap: 20px; /* Espaçamento entre as imagens */
    }

    .imagem_lado_a_lado img {
        height: 400px; /* Define a mesma altura para ambas as imagens */
        object-fit: cover; /* Garante que as imagens sejam cortadas proporcionalmente, sem distorção */
        border-radius: 5px; /* (Opcional) Adiciona bordas arredondadas às imagens */
    }
    .conjunto_alinhado {
        display: flex; /* Define um layout flexível */
        flex-direction: column; /* Organiza os itens em uma coluna */
        align-items: center; /* Centraliza os itens horizontalmente */
        gap: 20px; /* Espaçamento entre os elementos */
    }
</style>

<h2 style="text-align: center;">Reunião Geral com novos membros</h2>

Realizamos uma reunião geral com toda a equipe para mostrar mais detalhadamente o que é a iniciativa eVTOL, o que já conquistamos e o que queremos conquistar.
Esse encontro foi essencial para garantir que todos estejam cientes dos objetivos e desafios dos projetos e competições.

<div class="imagem_centrada">
    <img src="assets/img/reuniao_geral.jpeg" alt="Equipe reunida" width="800">
</div>
<br>

<h2 style="text-align: center;">Treinamento de Hardware</h2>

Como bixos, por natureza, não sabem de nada, nós os ajudamos dando um pontapé inicial para que não fiquem totalmente perdidos!
O primeiro treinamento foi o de hardware, feito com uma dinâmica que combinava prática e teoria com o objetivo de familizarizar os novos membros com o sistema dos nossos drones.

<div class="mexendo_drone">
    <img src="./assets/img/presidente_explicando.png" alt="Presidente explicando como mexer no drone">
    <div>
        <p>
            Durante o treinamento, foi apresentada a estrutura geral do drone - frame, hélices, motores brushless, ESCs, placas de distribuição, etc.
        </p>
        <ul>
            <li>Qual é a função da Raspberry PI? E da PixHawk?</li>
            <li>O que são sensores inerciais? Para que servem as câmeras?</li>
            <li>O que é odometria e o que é sensor fusion?</li>
        </ul>
        <h4 align="center">Tudo isso foi disutido nessa parte do treinamento!</h4>
        <br>
        <div class="imagem_centrada">
            <img src="./assets/img/mexendo_nos_drones.png" alt="Novos membros mexendo nos drones.">
        </div>
    </div>
</div>
<br>

<h2 style="text-align: center;">Treinamento de Software</h2>

Durante o treinamento de software, os ~~bixos~~ novos membros tiveram contato com a simulação do drone.
Foram abordados:

<div class="imagem_lado_a_lado">
    <img src="./assets/img/presidente_explicando.png" alt="Presidente explicando software">
    <img src="./assets/img/todos_no_treinamento_de_software.jpeg" alt="Foto de todos os participantes do treinamento">
</div>
<br>

<h2 style="text-align: center;">Alunos do ITA visitam SKYRATS</h2>

Nossa equipe realizou uma visita à skyrats, equipe de drones da USP. Essa interação fortaleceu nossa rede de colaboração estreitando laços entre os que virão a manter a indústria de drones do Brasil.

<div class="conjunto_alinhado">
    <div class="imagem_centrada">
        <img src="./assets/img/evtolITA_com_skyrats.jpeg" alt="Visita à equipe Skyrats" width="820">
    </div>
    <div class="imagem_lado_a_lado">
        <img src="./assets/img/zuffada.jpeg" alt="Imagem 1 da visita à Skyrats" width="400">
        <img src="./assets/img/lab_skyrats.jpeg" alt="Imagem 2 da visita à Skyrats" width="400">
    </div>
</div>
<br>
<div class="imagem_centrada">
        <video controls width="800" width="600">
            <source src="./assets/videos/theoffice_visita_skyrats.mp4" type="video/mp4">
        </video>
    </div>
<br>
<h3 style="text-align: center;">ZIPA DRONEZADA!!</h3>
<div class="imagem_lado_a_lado">
    <img src="./assets/img/van_skyrats.jpeg" alt="Imagem 1 da visita à Skyrats" width="400">
    <img src="./assets/img/van_skyrats2.jpeg" alt="Imagem 2 da visita à Skyrats" width="400">
</div>
<br>

<h2 style="text-align: center;">Montagem do Drone</h2>

<div class="mexendo_drone">
    <div class="imagem_centrada">
        <video controls width="800" width="250">
            <source src="./assets/videos/etapas_da_montagem_do_drone.mp4" type="video/mp4">
        </video>
    </div>
    <div>
        <p>Nesta etapa, realizamos a montagem de um dos drones, seguindo um planejamento detalhado para garantir a melhor performance e estabilidade.</p>
        <div class="imagem_centrada" >
            <img src="./assets/img/montagem_do_drone.jpeg" alt="Montagem do drone." width="600">
        </div>
    </div>
</div>
<br>

<h2 style="text-align: center;">Construção dos Alvos para a SAE</h2>

Para a classificatória da Robocup, confeccionamos alvos seguindo as especificações do regulamento.  
Esse processo envolveu corte, montagem e ajustes finais para garantir que os alvos estivessem dentro dos padrões exigidos.

<div class="imagem_centrada">
    <img src="./assets/img/" alt="Processo de montagem dos alvos">
</div>

<div class="imagem_centrada">
    <img src="./assets/img/" alt="Alvos finalizados">
</div>
<br>

<h2 style="text-align: center;">Manufatura da Peça de Suporte</h2>

Com toda a habilidade dos nossos membros, fizemos a modelagem em CAD para projetar a peça de suporte necessária para o suporte da bateria.

<div class="imagem_centrada">
    <img src="./assets/img/desenhos_cad_peca.png" alt="Desenhos CAD da peça">
</div>

<div class="imagem_centrada">
    <img src="./assets/img/peca_pronta.png" alt="Peça pronta">
</div>
<br>

<h2 style="text-align: center;">Calibração do PID</h2>

Nosso drone não cambaleia!  
Isso é **garantido** por nossa equipe!  
Estabilidade e precisão é o que se obtém após um trabalho bem feito na calibração do PID. Realizamos testes práticos para ajustar os parâmetros e obter a excelência no voo do nosso drone.

<div class="imagem_centrada">
    <video controls width="800">
        <source src="./assets/videos/calibracao_pid.mp4" type="video/mp4">
    </video>
</div>