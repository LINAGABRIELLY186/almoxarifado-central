# 📦 SIALM v1.0 — Sistema Integrado de Almoxarifado Municipal

> **Versão Legada (Monólito SSR):** Arquitetura baseada em Server-Side Rendering (SSR) utilizando **FastAPI**, **Jinja2**, **SQLite** e **Vanilla JavaScript**.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Jinja2](https://img.shields.io/badge/Jinja2-Template_Engine-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Chart.js](https://img.shields.io/badge/Chart.js-Data_Viz-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)

---

## 🎯 Contexto e Desafio

Na administração pública municipal, o controle de materiais de consumo e expediente (educação, saúde, infraestrutura e administração) frequentemente enfrenta gargalos operacionais devido ao uso de formulários manuais ou planilhas descentralizadas, gerando:

* Divergências entre saldo físico e registros de entrada/saída.
* Dificuldade de prestação de contas aos órgãos fiscalizadores e auditorias.
* Falta de padronização nas requisições entre secretarias e o almoxarifado central.

O **SIALM v1.0** foi concebido e implantado como uma solução centralizada, confiável e de baixo custo operacional para a **Prefeitura Municipal de Lagoa do Piauí**, informatizando todo o fluxo de suprimentos do município.

---

## 🏗️ Arquitetura da Versão 1.0 (Monólito SSR)

Para entregar uma solução funcional de forma rápida e com consumo mínimo de recursos de hardware no servidor local, optou-se pela abordagem de **Server-Side Rendering (SSR)**:

```text
               ┌────────────────────────────────────────────────────────┐
               │                     NAVEGADOR                          │
               │         (HTML5 semântico, CSS Dark Theme, JS)          │
               └───────────────▲────────────────────────▲───────────────┘
                               │ Requisição HTTP        │ Resposta HTML
                               ▼                        │
 ┌──────────────────────────────────────────────────────────────────────┐
 │                     FASTAPI APPLICATION SERVER                       │
 │                                                                      │
 │   ┌───────────────────────┐            ┌─────────────────────────┐   │
 │   │   Rotas / Endpoints   │ ─────────► │   Jinja2 Templates      │   │
 │   │   (Auth, Produtos,    │            │   (Componentes HTML,    │   │
 │   │    Movimentações,     │            │    Herança de layout,   │   │
 │   │    Relatórios)        │            │    Filtros de data)     │   │
 │   └───────────┬───────────┘            └─────────────────────────┘   │
 │               │                                                      │
 │               ▼                                                      │
 │   ┌───────────────────────┐                                          │
 │   │   SQLAlchemy ORM      │                                          │
 │   └───────────┬───────────┘                                          │
 └───────────────┼──────────────────────────────────────────────────────┘
                 ▼
       ┌───────────────────┐
       │   sialm.db        │
       │   (SQLite Engine) │
       └───────────────────┘
