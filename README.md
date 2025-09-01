# CICD_practice

Progetto di prova per capire come funziona CI/CD con Python e GitHub Actions.

## Badge CI

![Python Tests](https://github.com/waltpianist97/CICD_practice/actions/workflows/python-test.yml/badge.svg)

## Descrizione

Piccolo modulino Python con funzione `add(a, b)` e test associati usando `pytest`.  
Serve per vedere subito se i test passano/fallano in CI/CD.

## Struttura del progetto

CICD_practice/
├── mymodule.py
├── test/
│ └── test_mymodule.py
└── .github/
└── workflows/
└── python-test.yml

## Come usare in locale

1. Clona il repo:
   ```bash
   git clone https://github.com/tuo-username/CICD_practice.git
   cd CICD_practice
   ```
