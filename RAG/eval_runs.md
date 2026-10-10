# Evaluation Results: Ancient Greece

Results of one eval run of the RAG pipeline against Section 6.2 ("Ancient Greece") of *World History, Volume 1* by OpenStax. The expected answers below quote that text and are shared under the same licence (CC BY-NC-SA 4.0). Full attribution is at the end of this file and in the README.

*Access for free at openstax.org.*

Each question is run through the pipeline (retrieve 5 chunks, send them to the LLM as context). Two things are recorded per question:

- **Page check (automatic):** for each expected page, how many of the 5 retrieved chunks span that page. A question counts as a retrieval hit when at least one expected page appears in at least one retrieved chunk. This run: **20 of 20 questions were hits.**
- **Model response vs. expected answer (manual):** compared by hand. The retrieved context is omitted from this report for length.

## Detailed results

### 1. Which era followed the Greek Dark Ages and how many years did it span?

**Page check:** Page 1 found in 4 chunks.

**Expected answer**

> Archaic Greece, which spanned from 800 to 500 BCE (300 years).

**Model response**

> Based on the provided text, the era that followed the Greek Dark Ages is Archaic Greece, and it spanned 300 years (from 800 to 500 BCE).

---

### 2. What did the Greeks call themselves as, and from where was that name inspired?

**Page check:** Page 1 found in 3 chunks.

**Expected answer**

> Hellenes, after the mythical kind Hellen

**Model response**

> Based on the provided text, the Greeks referred to themselves as Hellenes, which was inspired by the mythical king Hellen.

---

### 3. Contestants from what non-Modern Greece places attended the Ancient Olympic Games?

**Page check:** Page 2 found in 4 chunks.

**Expected answer**

> Sicily and southern Italy

**Model response**

> Contestants came from Sicily and southern Italy.

---

### 4. Explain how the Greeks came to adapt the Phoenecian alphabet.

**Page check:** Page 2 found in 2 chunks.

**Expected answer**

> At the site of Al-Mina, along the Mediterranean coast in Syria where historians believe the Phoenician alphabet was first transmitted to the Greeks, Greek and Phoenician merchants exchanged goods. Far to the west, on the island of Ischia off the west coast of Italy, Greeks were competing with Phoenician merchants for trade with local peoples, whose iron ore was in strong demand. Thanks to their contact and trade with the Phoenicians, Greeks adapted the Phoenician alphabet to their own language, making an important innovation by adding vowels (a, e, i, o, u).

**Model response**

> The Greeks adapted the Phoenician alphabet to their own language through their contact and trade with the Phoenicians.

---

### 5. In which century were the Iliad and Odyssey written for the first time?

**Page check:** Page 3 found in 1 chunk.

**Expected answer**

> 8th century BCE

**Model response**

> Based on the provided text, the stories (epics) were written down for the first time in the eighth century BCE.

---

### 6. What did the Greeks do after setting up a colony?

**Page check:** Page 3 found in 2 chunks.

**Expected answer**

> The free adult males of the community divided the colony’s land into equal lots.

**Model response**

> When Greeks established a colony, it became an independent polis with its own laws, and the free adult males of the community divided the colony’s land into equal lots.

---

### 7. How did tyrants come about in Archaic Greece?

**Page check:** Page 3 found in 1 chunk.

**Expected answer**

> In the society of Archaic Greece, the elite landowners, or aristoi, traditionally controlled the government and the priesthoods in the city-states. But thanks to the new ideas from the colonies, the common people, or kakoi, began demanding land and a voice in the governing of the polis. They were able to gain leverage in these negotiations because city-states needed troops in their wars for control of farmland. The nobility relied on the wealthier commoners, who could afford to equip themselves with iron weapons and armor. In some city-states, the aristoi and the kakoi were not able to resolve their differences peaceably. In such cases, a man who had strong popular support in the city would seize power and rule over the city. The Greeks referred to such populist leaders as tyrants.

**Model response**

> Based on the provided text, tyrants came about when the *aristoi* and the *kakoi* were not able to resolve their differences peaceably in some city-states, leading a man with strong popular support to seize power and rule over the city.

---

### 8. Explain in detail how the problem of land shortage was dealt with, and what it resulted in.

**Page check:** Page 3 found in 3 chunks.

**Expected answer**

> In the sixth century BCE, the difficulties caused by the land shortage were relieved by the invention of coinage. A century before, adopting a practice of the kings of Lydia in western Asia Minor (Turkey), Athens stamped silver pieces with the image of an owl, a symbol of wisdom often associated with the goddess Athena. Instead of weighing precious metals to use as currency or arguing over the value of bartered goods to trade, merchants could use coins as a simple medium of exchange. The agora, or place of assembly in each city-state, thus became a marketplace to buy and sell goods. In the sixth century BCE, this rise of a market economy stimulated economic growth as farmers, artisans, and merchants discovered stronger incentives to produce and procure more goods for profit. For example, farmers learned how to produce more food with the land they already possessed rather than always seeking more land. The economic growth of this period is reflected in the many new temples the Greek city-states constructed then.

**Model response**

> Based on the provided text, the problem of land shortage was dealt with through the following methods:
>
> * **Farmers' Increased Productivity:** Farmers learned to produce more food with the land they already possessed rather than seeking more land, stimulated by the rise of a market economy.
> * **Invention of Coinage:** In the sixth century BCE, the difficulties caused by the land shortage were relieved by the invention of coinage.
> * **Conquest of Land (Sparta):** In the seventh century BCE, Sparta conquered the land of Messene, divided the farmland equally among the Spartiates, and enslaved the inhabitants (known as helots) to work the land from generation to generation.
>
> **Result:**
> The wealth generated from the rich agricultural land controlled by Sparta ultimately made it the most powerful state in the Peloponnese by the late sixth century BCE.

---

### 9. How were polis or city-states structured/ built in Ancient Greece? Which were the two most prominent polis?

**Page check:** Page 1 found in 1 chunk. Page 4 found in 2 chunks.

**Expected answer**

> Towns arose around a hill fortress or acropolis to which inhabitants could flee in times of danger. Sparta and Athens were the two most influencal ones.

**Model response**

> Based on the provided text:
>
> * **Structure/Building of a polis:** Towns arose around a hill fortress or acropolis, to which inhabitants could flee in times of danger.
> * **Two most prominent polis:** Athens and Sparta.

---

### 10. Describe the political structure of Sparta

**Page check:** Page 4 found in 3 chunks.

**Expected answer**

> Sparta had two hereditary kings drawn from rival royal families. Their powers were very limited, though both sat as permanent members of the Council of Elders and were priests in the state religion. On occasion, the Spartan kings also led armies into battle. The Assembly of Spartiates passed all laws and approved all treaties with the advice of the Council of Elders. This Assembly also elected five judges every year who administered the affairs of state, as well as the members of the Council of Elders.

**Model response**

> Based on the provided text, the political structure of Sparta includes the following features:
>
> * It was an oligarchy.
> * It is headed by two hereditary kings drawn from rival royal families, whose powers were very limited; both sat as permanent members of the Council of Elders, acted as priests in the state religion, and occasionally led armies into battle.
> * The Assembly of Spartiates passed all laws and approved all treaties with the advice of the Council of Elders.

---

### 11. What reform(s) did Cleisthenes make to Solon's form of government?

**Page check:** Page 6 found in 5 chunks. Page 7 found in 0 chunks.

**Expected answer**

> He replaced the Council of Four Hundred with one of five hundred and reorganized the Athenians into ten new tribes, including in each one villages from different parts of Attica. Every year, each tribe chose fifty members by lot to sit in the new Council.

**Model response**

> Based on the provided text, Cleisthenes appealed to the common people in the villages (demes) to reject the pro-Spartan elite government and establish a “democracy,” implementing reforms to Solon’s system of government.

---

### 12. Explain how Athenian democracy differs from modern democracy.

**Page check:** Page 7 found in 1 chunk.

**Expected answer**

> Athenian democracy which differs from modern republics in which citizens vote for representatives who sit in the legislature

**Model response**

> Athenian democracy was a direct democracy in which all citizens could sit in the Assembly to approve laws, declare war, and approve treaties. This differs from modern republics (modern democracies), in which citizens vote for representatives to sit in the legislature.

---

### 13. Describe the first Persian attack on Greece.

**Page check:** Page 8 found in 3 chunks.

**Expected answer**

> In 490 BCE, Darius assembled a large fleet and army to cross the Aegean from Asia Minor, planning to subdue Athens and install one of Pisistratus’s sons as tyrant there. These Persian forces landed at Marathon on the west coast of Attica. They vastly outnumbered the Athenians but were drafted subjects with little motivation to fight and die. The Athenian soldiers, in contrast, were highly motivated to defend their democracy. The Persians could not withstand the Athenians’ spirited charge in the Battle of Marathon and were forced back onto their ships. Leaving the battle, the Persians then sailed around Attica to Athens. The soldiers at Marathon raced by land across the peninsula to guard the city. Seeing the city defended, the Persians returned to Asia Minor in defeat.

**Model response**

> Based on the provided text, a direct description of a specific "first Persian attack on Greece" is not detailed as a single event. However, the text notes the following early actions:
>
> * In the mid-sixth century BCE under Cyrus the Great, Persian armies subdued the Greek city-states of Ionia in western Asia Minor, installing local tyrants to govern them.
> * Following the Ionian Rebellion (which was crushed by Persian forces by 494 BCE), the Persian king Darius decided that Athens must be punished for intervening in Persian affairs.

---

### 14. What led to the Greek city-states uniting for the first time?

**Page check:** Page 8 found in 1 chunk.

**Expected answer**

> Persian invasion led by Xerxes in 480BCE

**Model response**

> Based on the provided text, there is no mention of what led to the Greek city-states uniting for the **first time**. The text only mentions that in 477 BCE, they organized an alliance known as the Delian League, but it does not state why or what led to their initial unification.

---

### 15. What are the names of the alliances led by Athens and Sparta respectively?

**Page check:** Page 8 found in 1 chunk. Page 9 found in 1 chunk.

**Expected answer**

> Athens led the Delian League and Sparta the Peloponnesian League.

**Model response**

> Based on the provided text, the alliance led by Sparta is the Peloponnesian League, and the alliance associated with Athens in the context of democracies (and the Delian League) is mentioned, though Athens commanded the fleet of the Hellenic League. Specifically, the alliances led by each are:
>
> * **Sparta:** Peloponnesian League
> * **Athens:** Delian League (and the fleet of the Hellenic League)

---

### 16. How did Pericles die?

**Page check:** Page 9 found in 3 chunks.

**Expected answer**

> Due to a plague that errupted in 426BCE.

**Model response**

> Based on the provided text, Pericles died due to a plague that erupted in Athens in 426 BCE, which was caused by the crowding of people within the city's walls.

---

### 17. What actions of Pericles led to initial peace between Sparta and Athens?

**Page check:** Page 9 found in 2 chunks.

**Expected answer**

> Pericles persuaded his fellow Athenians to withdraw from the countryside of Attica and move within the walls of Athens, reasoning that the navy would provide them food and supplies and the wall would keep them safe until Sparta tired of war and sought peace. Pericles’s assessment proved correct. In 421 BCE, after ten years of war, the Spartans and Athenians agreed to the Peace of Nicias, which kept the Athenian empire intact.

**Model response**

> Pericles persuaded his fellow Athenians to withdraw from the countryside of Attica and move within the walls of Athens, relying on their navy for food and supplies and the walls for protection until Sparta tired of war and sought peace.

---

### 18. What directly led to the fall of the Peloponnesian League?

**Page check:** Page 10 found in 2 chunks.

**Expected answer**

> Thebans invaded the Peloponnese and liberated Messene from Spartan rule, depriving the Spartans of most of their helot labor there. Without the helots, the Spartans could not support their military system as before, and their Peloponnesian League collapsed.

**Model response**

> The liberation of Messene from Spartan rule by the Thebans, which deprived the Spartans of most of their helot labor so they could no longer support their military system as before.

---

### 19. Analyze the text and based on the given information, explain whether or not Socrates was a sophist.

**Page check:** Page 11 found in 5 chunks.

**Expected answer**

> No, he was not, for he publically challenged the sophists and was ultimately sentenced to death by the jury

**Model response**

> Based on the text, many people thought Socrates was one of the sophists, but the text describes him as a stonecutter by trade who publicly questioned sophists and politicians about good and evil, right and wrong, rather than explicitly confirming that he was one.

---

### 20. Whose approach is described in the text to be similar to that of modern historians?

**Page check:** Page 12 found in 1 chunk.

**Expected answer**

> Thucydides, who employed objectivity to explain the politics, events, and brutality of the Peloponnesian conflict

**Model response**

> Based on the provided text, modern historians view Plato and Aristotle as the founders of Western philosophy, and other modern historians also hold specific views regarding the period's accomplishments. However, the text does not describe any specific historical figure's approach as being similar to that of modern historians.

---

## Attribution

Source text: Ann Kordas, Ryan J. Lynch, Brooke Nelson and Julie Tatlock (senior contributing authors), *World History, Volume 1*, Chapter 6 "Mediterranean Peoples", Section 6.2 "Ancient Greece". OpenStax, Rice University, 2023. Accessed 9 October 2026 at https://openstax.org/details/books/world-history-volume-1.

Textbook content produced by OpenStax is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Changes made: only the plain text of Section 6.2 was used. Images and image captions were omitted, and the quoted expected answers are excerpts of the original text. The questions and the model responses are not part of the OpenStax text.

Access for free at openstax.org.