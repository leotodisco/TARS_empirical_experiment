# 🧪 Roadmap per la Valutazione In-Vitro di TARS

## **Fase 1: Progettazione dello Studio**

### 1. 🎯 Definizione degli Obiettivi e Domande di Ricerca

- **RQ1:** L’uso di TARS migliora la comprensione del codice rispetto alla condizione di controllo?
- **RQ2:** Come viene percepito TARS dagli utenti in termini di utilità, facilità d’uso e carico cognitivo?
- **RQ3:** TARS riesce ad adattare le spiegazioni alle caratteristiche individuali dell’utente (es. esperienza, intenzione, stile)?

- **RQ1:** Ipotesi e variabili:
- Variabile Tempo di spiegazione condizione di controllo (task fatto a mano senza internet nè IA)
- Variabile tempo per la spiegazione condizione con TARS
- ipotesi nulla: non c'è una significativa differenza nel tempo di comprensione del codice fra le due condizioni
- ipotesi alternativa: c'è significativa differenza

- **RQ2:** Come viene percepito TARS dagli utenti in termini di utilità, facilità d’uso e carico cognitivo?
- TAM PU
  TAM PE
  TAM BI
  TAM ATU
  NASA-TLX MentalDemand
  NASA-TLX PhysicalDemand
  NASA-TLX Performance
  NASA-TLX Effort
  NASA-TLX Frustrazione
  Feedback FB
- ipotesi nulla: Gli utenti non percepiscono differenze significative rispetto al valore neutro della scala (es. 3 su 0–5, oppure 5 su 0–10) nei punteggi di:

- **TAM**

  - **Utilità (PU)**: μ > μ₀ → TARS è percepito come utile.
  - **Facilità d’uso (PE)**: μ > μ₀ → TARS è percepito come facile da usare.
  - **Attitudine (ATU)**: μ > μ₀ → gli utenti hanno un atteggiamento positivo verso l’uso di TARS.
  - **Intenzione d’uso (BI)**: μ > μ₀ → gli utenti mostrano una maggiore intenzione a usare TARS.

- **NASA-TLX**

  - **Mental Demand (MD)**: μ < μ₀ → TARS riduce il carico mentale.
  - **Physical Demand (PD)**: μ < μ₀ → TARS riduce il carico fisico.
  - **Performance (P)**: μ > μ₀ → TARS migliora la performance percepita.
  - **Effort (E)**: μ < μ₀ → TARS richiede meno sforzo.
  - **Frustrazione (F)**: μ < μ₀ → TARS riduce la frustrazione.

- **RQ3:** TARS riesce ad adattare le spiegazioni alle caratteristiche individuali dell’utente (es. esperienza, intenzione, stile)?
- **Ipotesi nulla (H₀):**  
  TARS non adatta le spiegazioni alle caratteristiche individuali degli utenti (esperienza, intenzione, stile).  
  Le spiegazioni risultano indipendenti da tali caratteristiche.

- **Ipotesi alternativa (H₁):**  
  TARS adatta le spiegazioni alle caratteristiche individuali degli utenti (esperienza, intenzione, stile).  
  Le spiegazioni variano significativamente in funzione di queste caratteristiche.

TOM_1 TARS adapted the explanations to my level of programming experience Likert
TOM_2 I felt that TARS was adapting to the way I think.
TOM_3 TARS provided explanations that reflected the information I gave at the beginning (e.g., my experience level, goals, and preferences).
TOM_4 I would say that TARS successfully built a mental model of me as a user.
TOM_5 The tone used by TARS matched my selected preference (e.g., friendly, professional, neutral).
TOM_6 The explanations aligned with my main goals (e.g., learning, productivity, understand code...)
TOM_7 TARS respected my preferred explanation style (e.g., short/direct or detailed/technical).
TOM_8 Overall, I felt that TARS adapted its behavior to suit me as an individual user.
TOM_9 Compared to other tools, TARS felt more tailored to my needs.

---

### 2. 🧪 Scelta del Design dello Studio

- **Design:** Within-subject
- **Condizioni:** Ogni partecipante completa due task (uno con TARS, uno senza)
- **Obiettivo:** Confronto diretto tra performance (in termini sia di tempo per comprendere il codice che di bontà delle speigazioni fornite in quanto tali spiegazioni dell'utente vengono confrontate con un oracolo) e percezioni dello stesso utente

---

### 3. 🛠️ Preparazione degli Strumenti

- **Snippet di Codice:**  
  4 snippet di codice JAVA. Abbiamo scelto Java poichè è il linguaggio che tipicamente gli studenti della nostra università conoscono meglio.
  i codici sono estratti dal dataset chiamato CodeSearchNet composto da coppie <codice, spiegazione>. Tipicamente per spiegazione gli autori intendono la stringa di documentazione. Il dataset fa parte del framework di benchmark CodexGlue.
  Da questo dataset, che è gigante, ci sono centinaia di migliaia di entry, abbiamo campionato un subset nel seguente modo:
  Abbiamo computato la cyclomatic_complexity per ogni snippet usando la libreria lizard in python
  Poi abbiamo campionato in modo randomico 4 snippets e sono stati anche valutati a mano da noi in modo che pensassimo che il codice fosse complicato ma non troppo. Infatti come valore di ciclomatic complexity abbiamo preso gli snippet che avevano fra 10 e 30.

  Ogni partecipante vede tutti i 4 snippet di codice e gli viene assegnato un numero di combinazione (i numeri di combinazione vanno da 1 a 6). Per combinazine intendiamo: esempio combinazione 1: fai il task usando TARS sugli snippet 1 e 3 e fai il task a mano sugli snippet 2 e 4.
  Inoltre la popolazione dell'esperimento è splittata in modo che la metà dei partecipanti compie l'esperimento prima usando TARS e poi a mano, mentre la restante metà effettua prima a mano e poi con TARS.

  Andiamo a collezionare, per ogni task per ogni utente: tempo di completamento per fornire una spiegazione usando TARS + l'effettiva spiegazione e tempo di completamento per fornire una spegazione senza aiuto di TARS quindi in modo totalmente manuale + la spiegazione in sè.
  In tutti gli script Java sono stati rimossi i commenti in modo da non introdurre dei BIAS.

- **Quiz di Comprensione:**  
  Domande chiuse (max. 10 minuti).  
  Valutano comprensione semantica e funzionale dello snippet.

- **Questionari di Percezione:**
  - **TAM** (Technology Acceptance Model)
  - **NASA-TLX** (Task Load Index)
  - **Feedback qualitativo**

---

## **Fase 2: Conduzione dello Studio**

### 1. 👥 Reclutamento dei Partecipanti

- **Target:** 18 partecipanti tra: Studenti universitari triennale,Studenti universitari maglistrale, Ricercatori, Professionisti

---

### 2. 📋 Sessioni Sperimentali

- **Fasi della Sessione:**

  - Briefing iniziale - spiegazione a voce di cosa si deve fare e poi viene fornito il protocollo a ognuno dei partecipanti
  - Task 1 (TARS o controllo)
  - Task 2 (condizione opposta)
  - Survey post-esperimento

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

`QuizScore ~ Condition + ProgrammingExperience + LLMFamiliarity + (1 | Participant)`

### Mixed-Effects Model

🧩 Sottogruppi (opzionale)
• Split in Bassa/Alta esperienza
• Verifica interazioni Condition × Experience

📌 Interpretazione
• ↑ QuizScore → TARS migliora comprensione
• ↓ TaskTime → TARS più efficiente
• Effetto su novizi → supporto più utile ai meno esperti

📤 Output
• Tabella comparativa
• Violin/bar plot
• Osservazioni soggettive

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
   - Analisi per singole dimensioni: _Effort_, _Frustration_, ecc.

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
   - Domanda Likert: _"La spiegazione era adatta al tuo livello?"_
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
   - Dividi partecipanti in _Principianti_ vs _Esperti_
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
