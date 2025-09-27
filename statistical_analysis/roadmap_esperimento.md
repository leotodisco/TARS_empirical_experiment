# 🧪 Roadmap per la Valutazione In-Vitro di TARS

## **Fase 1: Progettazione dello Studio**

### 1. 🎯 Definizione degli Obiettivi e Domande di Ricerca

- **RQ1:** L’uso di TARS migliora la comprensione del codice rispetto alla condizione di controllo?
- **RQ2:** Come viene percepito TARS dagli utenti in termini di utilità, facilità d’uso e carico cognitivo?
- **RQ3:** TARS riesce ad adattare le spiegazioni alle caratteristiche individuali dell’utente (es. esperienza, intenzione, stile)?

---

### 2. 🧪 Scelta del Design dello Studio

- **Design:** Within-subject
- **Condizioni:** Ogni partecipante completa due task (uno con TARS, uno senza)
- **Obiettivo:** Confronto diretto tra performance e percezioni dello stesso utente

---

### 3. 🛠️ Preparazione degli Strumenti

- **Snippet di Codice:**  
  5 snippet Python (da repo open-source), selezionati per richiedere conoscenze di dominio (es. NLP, pandas). Rimuovi i commenti per aumentare la necessità di comprensione.

- **Quiz di Comprensione:**  
  Domande chiuse (max. 10 minuti).  
  Valutano comprensione semantica e funzionale dello snippet.

- **Questionari di Percezione:**  
  - **TAM** (Technology Acceptance Model)
  - **NASA-TLX** (Task Load Index)
  - **Feedback qualitativo** (opzionale)

---

## **Fase 2: Conduzione dello Studio**

### 1. 👥 Reclutamento dei Partecipanti

- **Target:** Studenti universitari con bassa esperienza di programmazione
- **Metodo:** Campionamento di convenienza (presentazioni, gruppi, contatti)
- **Pre-screening:**  
  - Programmazione (scala 1–10)  
  - Familiarità con LLM (bassa/moderata/alta)

---

### 2. 📋 Sessioni Sperimentali

- **Bilanciamento dei Gruppi:**  
  Ordine delle condizioni bilanciato per varianza su esperienza e LLM familiarity

- **Fasi della Sessione:**  
  - Briefing iniziale
  - Task 1 (TARS o controllo)
  - Quiz di comprensione
  - Task 2 (condizione opposta)
  - Quiz di comprensione
  - Survey post-esperimento

- **Tempi limite:**  
  - 20 min per ogni task  
  - 10 min per quiz

---

## **Fase 3: Analisi dei Dati**

---

### 🔍 **Analisi della Comprensione del Codice (per RQ1)**

#### 📌 Obiettivo

Valutare se TARS migliora la comprensione del codice rispetto alla condizione di controllo.

#### 🧪 Variabili

- **Indipendente:** `Condition` (TARS vs Control)
- **Dipendenti:**  
  - QuizScore (0–100%)  
  - TaskTime (secondi)  
  - SelfComprehension (Likert 1–5)
- **Covariate:**  
  - ProgrammingExperience (1–10)

#### 🔬 Disegno

- Design within-subject
- Controbilanciamento ordine
- Due snippet bilanciati

#### 📈 Analisi Statistica

1. **Assunzioni**  
   - Shapiro-Wilk (normalità)  
   - IQR per outlier su tempo

2. **Test**  
   - T-test appaiato o Wilcoxon

3. **Effetto**  
   - Cohen’s d_z o r  
   - CI al 95% (bootstrap)

#### 📊 Regressione

```QuizScore ~ Condition + ProgrammingExperience + LLMFamiliarity + (1 | Participant)```

### Mixed-Effects Model

🧩 Sottogruppi (opzionale)
	•	Split in Bassa/Alta esperienza
	•	Verifica interazioni Condition × Experience

📌 Interpretazione
	•	↑ QuizScore → TARS migliora comprensione
	•	↓ TaskTime → TARS più efficiente
	•	Effetto su novizi → supporto più utile ai meno esperti

📤 Output
	•	Tabella comparativa
	•	Violin/bar plot
	•	Osservazioni soggettive

## 🧠 Analisi delle Percezioni (per RQ2)

### 📌 Obiettivo
Indagare l’esperienza utente in termini di:
- **Utilità percepita** (PU)
- **Facilità d’uso** (PEOU)
- **Carico cognitivo** (NASA-TLX)

---

### 🧪 Strumenti
- **TAM** – Technology Acceptance Model (scala Likert 1–7)
- **NASA-TLX** – Task Load Index (versione completa o semplificata)
- **Domande aperte** per raccogliere feedback qualitativo

---

### 🧪 Somministrazione
- Dopo **ciascun task** (con e senza TARS)
- Survey **comparativa finale** al termine dell’esperimento

---

### 📈 Analisi Statistica

1. **TAM (PU, PEOU)**
   - T-test appaiato oppure Wilcoxon signed-rank test (se non normale)

2. **NASA-TLX**
   - Calcolo del punteggio medio
   - Analisi per singole dimensioni: *Effort*, *Frustration*, ecc.

3. **Effetto**
   - Calcolo di p-value e **Cohen’s dₚ**
   - Visualizzazione con boxplot o barre con **intervallo di confidenza (CI)**

---


### 📌 Interpretazione
- **PU e PEOU alti** → TARS è percepito come utile e facile da usare
- **NASA-TLX più basso** → TARS riduce il carico cognitivo rispetto al controllo

---

### 📤 Output Attesi
- Tabelle comparate dei punteggi TAM & TLX
- Grafici comparativi (boxplot, barre con CI)
- Sintesi tematica dei commenti qualitativi

---

## 🧩 Analisi dell’Adattività (per RQ3)

### 📌 Obiettivo
Verificare se TARS adatta le spiegazioni al profilo dell’utente.

---

### 🧪 Variabili

1. **Profilo Utente**
   - `ProgrammingExperience` (scala 1–10)
   - `LLMFamiliarity` (scala 1–5)

2. **Spiegazioni Generate da TARS**
   - Codifica secondo:
     - **Livello tecnico** (base, intermedio, avanzato)
     - **Tono** (formale, amichevole, didattico)
     - **Focalizzazione** (scopo generale vs dettagli tecnici)
     - **Formato** (paragrafo, elenco, misto)

3. **Percezione dell’adattività**
   - Domanda Likert: *"La spiegazione era adatta al tuo livello?"*
   - Risposte aperte per motivare la valutazione

---

### 🧩 Codifica delle Spiegazioni
- Due valutatori indipendenti codificano un sottoinsieme
- Categorie:
  - Lessico usato (termini tecnici, semplificazioni)
  - Profondità della spiegazione
  - Stile comunicativo (diretto, analogico, esemplificativo)
- Verifica coerenza tra **profilo utente** e **caratteristiche della spiegazione**

---

### 📈 Analisi Statistica

1. **Correlazioni**
   - **Spearman’s rho** tra:
     - Esperienza ↔ livello tecnico della spiegazione
     - Familiarità ↔ formato/tono
     - Percezione ↔ codifica oggettiva

2. **Analisi per gruppi**
   - Dividi partecipanti in *Principianti* vs *Esperti*
   - Confronta:
     - Spiegazioni ricevute
     - Valutazioni soggettive di adattività

---

### 📊 Analisi Qualitativa
Categorizza le risposte aperte in base a:
- “**Troppo semplice**” o “**troppo tecnica**”
- “**Adatta al mio livello**”
- “**Vorrei più esempi/metafore**”

---

### 📌 Interpretazione
- **Alto allineamento** spiegazione ↔ profilo → TARS è adattivo
- **Scarsa corrispondenza** → generazione troppo generica o non personalizzata
- Effetti più evidenti nei **novizi** → maggiore beneficio della personalizzazione

---

### 📤 Output Attesi
- Matrice: `Profilo utente` ↔ `Caratteristiche spiegazione`
- Grafico di dispersione: esperienza vs adattività percepita
- **Quote qualitative** rappresentative (per illustrare ciascuna categoria)

---

In tommy Sono stati applicati due modelli standard per la valutazione:
- Il Technology Acceptance Model (TAM) per misurare l'utilità percepita e la facilità d'uso percepita.
- Il Task Load Index (NASA-TLX) per valutare il carico cognitivo.
- Feedback Qualitativo Aperto: Oltre alle metriche quantitative, è stato raccolto feedback qualitativo aperto dopo il completamento di ciascun compito. Questo feedback è stato poi analizzato utilizzando il metodo del card sorting. Questo tipo di feedback non deriva da domande strutturate predefinite, ma da commenti liberi degli utenti.
- ho notato che per tommy hanno fatto prima uno screening dei soggetti, dovremmo farlo anche noi?
- in tommy c'erano 15 persone