---
char_name: Valerius
species: Satyr
class: Paladin
level: 6
subclass: Oath of Devotion
background: Planar Envoy
alignment: Chaotic Good
xp_current: 14000
xp_next: 23000
base_str: 17
base_dex: 12
base_con: 14
base_int: 11
base_wis: 13
base_cha: 15
str_bonus: 1
dex_bonus: 0
con_bonus: 0
int_bonus: 0
wis_bonus: 0
cha_bonus: 3
prof_bonus: 3
cloak_bonus: 1
plate_ac: 18
shield_ac: 2
defense_style: 1
base_hp_total: 39
hp_current: 51
hp_temp: 0
slot_1_1: true
slot_1_2: true
slot_1_3: true
slot_1_4: true
slot_2_1: true
slot_2_2: true
---
# ⚔️ D&D 5e (2024) Character Sheet

<a id="character-info"></a>
## Character Information
| Header | Details |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Character Name** | `VIEW[{char_name}]` |
| **Species** | [Satyr](../../Race/Race_Satyr.md) (Fey) |
| **Class & Level** | Paladin <span id="paladin-level">`VIEW[{level}]`</span> (Oath of Devotion) (Total Level: <span id="total-level">`VIEW[{level}]`</span>) |
| **Background** | [Planar Envoy](../../Backgrounds/Custom/Background_Planar%20Envoy.md) |
| **Alignment** | `VIEW[{alignment}]` |
| **Proficiency Bonus** | <span id="prof-bonus">+`VIEW[{prof_bonus}]`</span> |
| **Experience Points** | `VIEW[{xp_current}]` / `VIEW[{xp_next}]` |
| **Hit Die** | <span id="hit-die-type">`VIEW[{hit_die_type}]`</span> |
| **Base HP (Rolled)** | <span id="base-hp-formula">10 (base max) + 3 + 5 + 4 + 7 + 10</span> = **<span id="base-hp-total">`VIEW[{base_hp_total}]`</span>** |
| **Base Stats (Rolled)** | **STR:** <span id="base-str">17</span>, **DEX:** <span id="base-dex">12</span>, **CON:** <span id="base-con">14</span>, **INT:** <span id="base-int">11</span>, **WIS:** <span id="base-wis">13</span>, **CHA:** <span id="base-cha">15</span> |

---

<a id="ability-scores"></a>
## 📊 Ability Scores & Saving Throws
| Ability | Score | Mod | Save | Skills |
| -------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **STR** Strength | `VIEW[{base_str}]` + `VIEW[{str_bonus}]` = **`VIEW[{base_str} + {str_bonus}]`** | <span id="str-mod">**+`VIEW[floor(({base_str} + {str_bonus} - 10) / 2)]`**</span> | +`VIEW[floor(({base_str} + {str_bonus} - 10) / 2)]` + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` (Aura) + `VIEW[{cloak_bonus}]` (Cloak) = **+`VIEW[floor(({base_str} + {str_bonus} - 10) / 2) + floor(({base_cha} + {cha_bonus} - 10) / 2) + {cloak_bonus}]`** | [x] Athletics (+`VIEW[floor(({base_str} + {str_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` = +`VIEW[floor(({base_str} + {str_bonus} - 10) / 2) + {prof_bonus}]`) |
| **DEX** Dexterity | `VIEW[{base_dex}]` = **`VIEW[{base_dex}]`** | <span id="dex-mod">**+`VIEW[floor(({base_dex} + {dex_bonus} - 10) / 2)]`**</span> | +`VIEW[floor(({base_dex} + {dex_bonus} - 10) / 2)]` + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` (Aura) + `VIEW[{cloak_bonus}]` (Cloak) = **+`VIEW[floor(({base_dex} + {dex_bonus} - 10) / 2) + floor(({base_cha} + {cha_bonus} - 10) / 2) + {cloak_bonus}]`** | [ ] Acrobatics (+`VIEW[floor(({base_dex} + {dex_bonus} - 10) / 2)]`) <br> [ ] Sleight of Hand (+`VIEW[floor(({base_dex} + {dex_bonus} - 10) / 2)]`) <br> [ ] Stealth (+`VIEW[floor(({base_dex} + {dex_bonus} - 10) / 2)]`)* |
| **CON** Constitution | `VIEW[{base_con}]` = **`VIEW[{base_con}]`** | <span id="con-mod">**+`VIEW[floor(({base_con} + {con_bonus} - 10) / 2)]`**</span> | +`VIEW[floor(({base_con} + {con_bonus} - 10) / 2)]` + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` (Aura) + `VIEW[{cloak_bonus}]` (Cloak) = **+`VIEW[floor(({base_con} + {con_bonus} - 10) / 2) + floor(({base_cha} + {cha_bonus} - 10) / 2) + {cloak_bonus}]`** | — |
| **INT** Intelligence | `VIEW[{base_int}]` = **`VIEW[{base_int}]`** | <span id="int-mod">**+`VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]`**</span> | +`VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]` + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` (Aura) + `VIEW[{cloak_bonus}]` (Cloak) = **+`VIEW[floor(({base_int} + {int_bonus} - 10) / 2) + floor(({base_cha} + {cha_bonus} - 10) / 2) + {cloak_bonus}]`** | [ ] Arcana (+`VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]`) <br> [ ] History (+`VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]`) <br> [ ] Investigation (+`VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]`) <br> [ ] Nature (+`VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]`) <br> [x] Religion (+`VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` = +`VIEW[floor(({base_int} + {int_bonus} - 10) / 2) + {prof_bonus}]`) |
| **WIS** Wisdom | `VIEW[{base_wis}]` = **`VIEW[{base_wis}]`** | <span id="wis-mod">**+`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]`**</span> | +`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` (Prof) + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` (Aura) + `VIEW[{cloak_bonus}]` (Cloak) = **+`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2) + {prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2) + {cloak_bonus}]`** | [x] Insight (+`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` = +`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2) + {prof_bonus}]`) <br> [ ] Animal Handling (+`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]`) <br> [ ] Medicine (+`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]`) <br> [ ] Perception (+`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]`) <br> [ ] Survival (+`VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]`) |
| **CHA** Charisma | `VIEW[{base_cha}]` + 2 + 1 = **`VIEW[{base_cha} + {cha_bonus}]`** | <span id="cha-mod">**+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]`**</span> | +`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` (Prof) + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` (Aura) + `VIEW[{cloak_bonus}]` (Cloak) = **+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2) * 2 + {prof_bonus} + {cloak_bonus}]`** | [x] Performance (+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` = +`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2) + {prof_bonus}]`) <br> [x] Persuasion (+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` = +`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2) + {prof_bonus}]`) <br> [ ] Deception (+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]`) <br> [x] Intimidation (+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` + `VIEW[{prof_bonus}]` = +`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2) + {prof_bonus}]`) |

*\* Stealth rolls are made with Disadvantage due to wearing Plate Armor.*

### 🧠 Passive Skills
- **Passive Perception:** 10 + `VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2)]` = **`VIEW[10 + floor(({base_wis} + {wis_bonus} - 10) / 2)]`**
- **Passive Insight:** 10 + `VIEW[floor(({base_wis} + {wis_bonus} - 10) / 2) + {prof_bonus}]` (Insight Proficient) = **`VIEW[10 + floor(({base_wis} + {wis_bonus} - 10) / 2) + {prof_bonus}]`**
- **Passive Investigation:** 10 + `VIEW[floor(({base_int} + {int_bonus} - 10) / 2)]` = **`VIEW[10 + floor(({base_int} + {int_bonus} - 10) / 2)]`**


---

<a id="combat-stats"></a>
## 🛡️ Combat Stats
| Stat | Value | Description |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Armor Class (AC)** | **`VIEW[{plate_ac} + {shield_ac} + {cloak_bonus} + {defense_style}]`** | [Plate (18)](../../Equipment/Equipment_Plate%20Armor.md) + [Shield (2)](../../Equipment/Equipment_Shield.md) + [Cloak (1)](../../MagicItems/MagicItem_Cloak%20of%20Protection.md) + [Defense Style (1)](../../Feats/Feat_Defense.md) = **22** |
| **Initiative** | **+`VIEW[floor(({base_dex} + {dex_bonus} - 10) / 2) + {prof_bonus}]`** | [Dex Modifier (+1)](#dex-mod) + [Proficiency Bonus (+3)](#prof-bonus) ([Alert Feat](#species-traits-feats)) |
| **Speed** | **35 ft.** | Base walking speed |
| **Hit Points (Max)** | **`VIEW[{base_hp_total} + {level} * floor(({base_con} + {con_bonus} - 10) / 2)]`** | [Base HP (39)](#base-hp-total) + [Paladin Level (6)](#paladin-level) × [Con modifier (+2)](#con-mod) = **51** |
| **Current Hit Points** | `INPUT[number:hp_current]` / `VIEW[{base_hp_total} + {level} * floor(({base_con} + {con_bonus} - 10) / 2)]` | `INPUT[slider(minValue(0), maxValue(51)):hp_current]` |
| **Temp Hit Points** | `INPUT[number:hp_temp]` | Temporary hit points |
| **Hit Dice** | **`VIEW[{level}]`[d10](#hit-die-type)** | Remaining: `[x] [x] [x] [x] [x] [x]` (d10 per [Paladin Level](#paladin-level)) |
| **Death Saves** | — | Successes: `[ ] [ ] [ ]` <br> Failures: `[ ] [ ] [ ]` |

---

<a id="weapons-attacks"></a>
## ⚔️ Weapons & Attacks
| Weapon / Attack | Attack Bonus | Damage | Damage Type / Properties | Mastery |
| --------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------- | -------- |
| **Moon-Touched Longsword** (One-Handed) | +**`VIEW[floor(({base_str} + {str_bonus} - 10) / 2) + {prof_bonus}]`** | **1d8 + `VIEW[floor(({base_str} + {str_bonus} - 10) / 2)]`** | Slashing (Magical, Moon-Touched) | **Sap** |
| **Ram (Unarmed Strike)** | +**`VIEW[floor(({base_str} + {str_bonus} - 10) / 2) + {prof_bonus}]`** | **1d6 + `VIEW[floor(({base_str} + {str_bonus} - 10) / 2)]`** | Bludgeoning (Satyr Species trait) | — |
| **Javelin** (Range 30/120) | +**`VIEW[floor(({base_str} + {str_bonus} - 10) / 2) + {prof_bonus}]`** | **1d6 + `VIEW[floor(({base_str} + {str_bonus} - 10) / 2)]`** | Piercing (Thrown) | **Slow** |

*Note: With **Sacred Weapon** active, add your Charisma modifier to attack rolls with your melee weapon (Total: +**`VIEW[floor(({base_str} + {str_bonus} - 10) / 2) + {prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2)]`** to hit).*

---

<a id="combat-actions"></a>
## 🔄 Combat Turn Actions (D&D 2024 Cheat Sheet)
On your turn in combat, you can take **one Action**, **one Bonus Action** (if available), **move up to your Speed**, and perform minor interactions. You can also take **one Reaction** per round in response to triggers.

### 🎬 Actions
You can perform one of the following Actions on your turn:
- **Attack:** Use a weapon to make a melee or ranged attack. You can attack twice instead of once when you take this action (Extra Attack).
  - [Moon-Touched Longsword Melee Attack](#weapons-attacks): **+7 to hit**, **1d8 + 4 slashing** damage. Applies [Sap](#paladin-features) mastery (target has Disadvantage on its next attack).
  - [Javelin Ranged Attack](#weapons-attacks) (Range 30/120): **+7 to hit**, **1d6 + 4 piercing** damage. Applies [Slow](#paladin-features) mastery (target speed reduced by 10 ft).
  - [Ram Melee Attack](#weapons-attacks): **+7 to hit**, **1d6 + 4 bludgeoning** damage.
- **Magic (Cast a Spell):** Cast a prepared spell that has a casting time of 1 Action.
  - [Protection from Evil and Good](../../Spells/Spell_Protection%20from%20Evil%20and%20Good.md): Concentration up to 10 min.
  - [Heroism](../../Spells/Spell_Heroism.md): Concentration up to 1 min.
  - [Cure Wounds](../../Spells/Spell_Cure%20Wounds.md): Heal a creature for **2d8 + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` HP**.
- **Turn the Unholy ([Channel Divinity](#channel-divinity)):** Present your Holy Symbol. Each Fiend or Undead within 30 feet must make a Wisdom Saving Throw ([DC 15](#spellcasting-divinity)) or be Turned for 1 minute.
- **Abjure Foes ([Channel Divinity](#channel-divinity)):** Present Spellcasting Focus. Choose up to 4 creatures within 60 feet. Each must make a Wisdom Saving Throw ([DC 15](#spellcasting-divinity)) or be Frightened (speed 0) for 1 minute (speed halved on save).
- **Sacred Weapon ([Channel Divinity](#channel-divinity)):** Imbue your melee weapon with positive energy (can also be done as part of the Attack action).
- **Dash:** Gain extra movement equal to your speed (35 feet) for the current turn.
- **Disengage:** Prevents Opportunity Attacks from moving away from enemies for the rest of the turn.
- **Dodge:** Attack rolls against you have Disadvantage, and you make Dexterity saving throws with Advantage.
- **Help:** Give an ally Advantage on their next ability check or attack roll.
- **Hide:** Make a Dexterity (Stealth) check (with Disadvantage due to Plate Armor) to become hidden.
- **Ready:** Set a trigger to perform a specific action as a Reaction later in the round.
- **Search:** Search for something using Wisdom (Perception) or Intelligence (Investigation).
- **Study:** Recall knowledge using an Intelligence-based skill (Religion, History, etc.).
- **Influence:** Attempt to influence creatures using Charisma-based skills (Persuasion, Performance, etc.).
- **Use an Object:** Use an item or interact with a second object.

### ⚡ Bonus Actions
You can take a Bonus Action only when a special ability or spell specifies that you can do so. You can take only one Bonus Action on your turn:
- **Lay on Hands:** Touch a creature and restore HP or cure the Poisoned condition. See [Lay on Hands](#paladin-features).
- **Divine Sense ([Channel Divinity](#channel-divinity)):** Detect celestials, fiends, and undead within 60 feet for 10 minutes.
- **Sacred Weapon ([Channel Divinity](#channel-divinity)):** Imbue your melee weapon with positive energy for 10 minutes.
- **Divine Smite:** Cast [Divine Smite](../../Spells/Spell_Divine%20Smite.md) (casting time: 1 Bonus Action) immediately after hitting a creature with a melee weapon or unarmed strike to deal extra radiant damage.
- **Spellcasting:** Cast a prepared spell that has a casting time of 1 Bonus Action:
  - [Shield of Faith](../../Spells/Spell_Shield%20of%20Faith.md): Concentration up to 10 minutes, +2 to AC.

### ↩️ Reactions
You can take one Reaction per round, inside or outside your turn, in response to a specific trigger:
- **Opportunity Attack:** Make a melee weapon attack against a hostile creature that moves out of your reach.
- **Reactive Spell ([War Caster Feat](#species-traits-feats)):** Cast a spell as a Reaction instead of making an Opportunity Attack (1 Action cast time, targets only that creature).
- **Readied Action:** Execute the action you prepared with the *Ready* action on your turn.

### 🏃 Movement & Other Activities
These can be done in tandem with your movement and actions:
- **Move:** Travel up to your Speed (35 feet), which can be broken up before, during, and after actions.
- **Mirthful Leaps ([Satyr Traits](#species-traits-feats)):** Roll a `d8` and add the result to your jump distance.
- **Interact with an Object:** Draw or sheathe a weapon, open a door, pick up an item (one free interaction per turn; additional interactions require the *Use an Object* action).

---

<a id="proficiencies-languages"></a>
## 🎒 Proficiencies & Languages
- **Armor:** Light Armor, Medium Armor, Heavy Armor, Shields
- **Weapons:** Simple Weapons, Martial Weapons
- **Tools:** Pan Flute (Species), Gaming Set or Musical Instrument of choice (Background)
- **Languages:** Common, Sylvan (Species), Infernal or Abyssal (Background)

---

<a id="species-traits-feats"></a>
## 🌟 Species Traits & Feats
### Satyr Species Traits
- **Creature Type:** Fey (not Humanoid; immune to spells like *Hold Person*).
- **Magic Resistance:** You have Advantage on saving throws against spells.
- **Mirthful Leaps:** When you make a long or high jump, roll a `d8` and add the result to the jump distance (costs movement as normal).
- **Reveler:** Proficiency in Performance and Persuasion skills, and Pan Flute.

### Origin Feat: [Alert](../../Feats/Feat_Alert.md) (Background)
- **Initiative Proficiency:** When you roll Initiative, you can add your Proficiency Bonus (+`VIEW[{prof_bonus}]`) to the roll.
- **Initiative Swap:** Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing ally in the same combat. You can't make this swap if you or the ally has the Incapacitated condition.

### Level 4 Feat: [War Caster](../../Feats/Feat_War%20Caster.md)
- **Ability Score Increase:** Increased Charisma by +1 (included in Charisma score).
- **Concentration:** You have Advantage on Constitution saving throws that you make to maintain Concentration.
- **Reactive Spell:** When a creature provokes an Opportunity Attack from you, you can take a Reaction to cast a spell at the creature instead of making an Opportunity Attack (1 Action cast time, targets only that creature).
- **Somatic Components:** You can perform Somatic components of spells even with your Moon-Touched Longsword and Shield in hand.


<a id="paladin-features"></a>
## 🛡️ Paladin Class Journey & Features

### ⚖️ Level 1
*   **[Lay on Hands](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%201:%20Lay%20On%20Hands)**: Pool of **`VIEW[5 * {level}]` HP** (5 × Paladin Level `VIEW[{level}]`). Restore HP or cure Poison.
*   **[Spellcasting](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%201:%20Spellcasting)**: Spell Save DC `VIEW[8 + {prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2)]`, Spell Attack +`VIEW[{prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2)]`.
*   **[Weapon Mastery](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%201:%20Weapon%20Mastery)**: Longsword (Sap), Javelin (Slow).

### ⚔️ Level 2
*   **[Fighting Style](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%202:%20Fighting%20Style) (Choice)**: Chosen **[Defense](../../Feats/Feat_Defense.md)** (+1 AC while wearing armor).
*   **[Paladin's Smite](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%202:%20Paladin's%20Smite)**: *Divine Smite* always prepared, 1 free cast per day.

### ☀️ Level 3
*   **[Channel Divinity](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%203:%20Channel%20Divinity)**: 2 uses per short/long rest.
*   **[Paladin Subclass](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%203:%20Paladin%20Subclass) (Choice)**: Chosen **[Oath of Devotion](../../Classes/Paladin/Subclasses/Sublcass_Paladin%20-%20Oath%20of%20Devotion.md)** subclass.

### 🌟 Level 4
*   **[Feat / ASI Choice](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%204:%20Ability%20Score%20Improvement)**: Chosen **[War Caster](../../Feats/Feat_War%20Caster.md)** feat (+1 Charisma).

### ⚡ Level 5
*   **[Extra Attack](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%205:%20Extra%20Attack)**: Attack twice instead of once with the Attack action.
*   **[Faithful Steed](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%205:%20Faithful%20Steed)**: *Find Steed* always prepared, 1 free cast per day.

### 🛡️ Level 6
*   **[Aura of Protection](../../Classes/Paladin/Paladin%20-%20D&D%205e%20%282024%29.md#Level%206:%20Aura%20of%20Protection)**: +4 to saving throws for you and friendly creatures within 10 feet.

---

<a id="spellcasting-divinity"></a>
## ✨ Spellcasting & Channel Divinity
| Spell Save DC | Spell Attack Bonus | Spell Slots |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`VIEW[8 + {prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2)]`** (8 + `VIEW[{prof_bonus}]` PB + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` CHA) | **+`VIEW[{prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2)]`** (`VIEW[{prof_bonus}]` PB + `VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]` CHA) | 1st Level: `INPUT[toggle:slot_1_1]` `INPUT[toggle:slot_1_2]` `INPUT[toggle:slot_1_3]` `INPUT[toggle:slot_1_4]` (4 Slots) <br> 2nd Level: `INPUT[toggle:slot_2_1]` `INPUT[toggle:slot_2_2]` (2 Slots) |

BUTTON[long-rest-btn]

```meta-bind-button
id: long-rest-btn
label: "🔋 Long Rest"
hidden: true
style: default
actions:
  - type: updateMetadata
    bindTarget: hp_current
    evaluate: true
    value: "51"
  - type: updateMetadata
    bindTarget: hp_temp
    evaluate: true
    value: "0"
  - type: updateMetadata
    bindTarget: slot_1_1
    evaluate: true
    value: "true"
  - type: updateMetadata
    bindTarget: slot_1_2
    evaluate: true
    value: "true"
  - type: updateMetadata
    bindTarget: slot_1_3
    evaluate: true
    value: "true"
  - type: updateMetadata
    bindTarget: slot_1_4
    evaluate: true
    value: "true"
  - type: updateMetadata
    bindTarget: slot_2_1
    evaluate: true
    value: "true"
  - type: updateMetadata
    bindTarget: slot_2_2
    evaluate: true
    value: "true"
```

<a id="channel-divinity"></a>
### Channel Divinity
You have **2 uses** of Channel Divinity per Short or Long Rest. Regain 1 expended use on a Short Rest, and all on a Long Rest.
- **Divine Sense** *(Bonus Action)*: Detect Celestials, Fiends, and Undead within 60 feet for 10 minutes.
- **Sacred Weapon** *(Attack Action / Bonus Action)*: Imbue your melee weapon with positive energy for 10 minutes. Add Charisma modifier (+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]`) to attack rolls (min +1). Weapon deals normal or Radiant damage and emits Bright Light in 20-foot radius. Ends early if dropped.
- **Turn the Unholy** *(Magic Action)*: Present your Holy Symbol. Each Fiend or Undead within 30 feet must succeed on a Wisdom saving throw (DC `VIEW[8 + {prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2)]`) or be Turned for 1 minute or until it takes damage.
- **Abjure Foes** *(Magic Action)*: Present your Spellcasting Focus and target a number of creatures within 60 feet equal to your Charisma modifier (+`VIEW[floor(({base_cha} + {cha_bonus} - 10) / 2)]`) (min 1). Each target must make a Wisdom saving throw (DC `VIEW[8 + {prof_bonus} + floor(({base_cha} + {cha_bonus} - 10) / 2)]`). On a failed save, a target is Frightened for 1 minute or until it takes damage; its speed is 0. On a successful save, its speed is halved for 1 minute or until it takes damage.

<a id="prepared-spells"></a>
### Prepared Spells (9 Prepared + Oath Spells + Paladin Features)

#### Paladin's Smite
| Spell | Level | Casting Time | Concentration | Duration |
| ---------------------------------------------------- | ----- | ------------ | ------------- | ------------- |
| [Divine Smite](../../Spells/Spell_Divine%20Smite.md) | 1 | Bonus Action | No | Instantaneous |

#### Faithful Steed
| Spell | Level | Casting Time | Concentration | Duration |
| ------------------------------------------------ | ----- | ------------ | ------------- | ------------- |
| [Find Steed](../../Spells/Spell_Find%20Steed.md) | 2 | Action | No | Instantaneous |

#### Oath Spells
| Spell | Level | Casting Time | Concentration | Duration |
| -------------------------------------------------------------------------------------------- | ----- | ------------ | ------------- | ------------------------------- |
| [Protection from Evil and Good](../../Spells/Spell_Protection%20from%20Evil%20and%20Good.md) | 1 | Action | ⚠️ Yes | Concentration up to 10 minutes |
| [Shield of Faith](../../Spells/Spell_Shield%20of%20Faith.md) | 1 | Bonus Action | ⚠️ Yes | Concentration, up to 10 minutes |
| [Aid](../../Spells/Spell_Aid.md) | 2 | Action | No | 8 hours |
| [Zone of Truth](../../Spells/Spell_Zone%20of%20Truth.md) | 2 | Action | No | 10 minutes |

#### Paladin Spellcasting (Prepared)
| Spell | Level | Casting Time | Concentration | Duration |
| ---------------------------------------------------------------- | ----- | ------------ | ------------- | ------------------------------- |
| [Bless](../../Spells/Spell_Bless.md) | 1 | Action | ⚠️ Yes | Concentration, up to 1 minute |
| [Cure Wounds](../../Spells/Spell_Cure%20Wounds.md) | 1 | Action | No | Instantaneous |
| [Heroism](../../Spells/Spell_Heroism.md) | 1 | Action | ⚠️ Yes | Concentration, up to 1 minute |
| [Thunderous Smite](../../Spells/Spell_Thunderous%20Smite.md) | 1 | Bonus Action | No | Instantaneous |
| [Wrathful Smite](../../Spells/Spell_Wrathful%20Smite.md) | 1 | Bonus Action | No | 1 minute |
| [Lesser Restoration](../../Spells/Spell_Lesser%20Restoration.md) | 2 | Bonus Action | No | Instantaneous |
| [Locate Object](../../Spells/Spell_Locate%20Object.md) | 2 | Action | ⚠️ Yes | Concentration, up to 10 minutes |

---

<a id="equipment-currency"></a>
## 🎒 Equipment & Currency

### 🛡️ Equipped Slots
| Slot | Equipped Item | Details / Properties |
| ------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **Armor** | [Plate Armor](../../Equipment/Equipment_Plate%20Armor.md) | AC 18, Stealth Disadvantage, Str 15 req. |
| **Main Hand** | [Moon-Touched Longsword](../../MagicItems/MagicItem_Moon%20Touched%20Sword.md) | Magic Weapon, 1d8+4 slashing (Versatile 1d10), Sap, Sheds Light |
| **Off-Hand** | [Shield](../../Equipment/Equipment_Shield.md) | AC +2 |

### 🔮 Tuned Magic Items Status
- **Status:** `1 / 3` active slots used
- **Tuned Items:**
  - `1.` [Cloak of Protection](../../MagicItems/MagicItem_Cloak%20of%20Protection.md) (+1 to AC and all saving throws)

### 🎒 Carrying Inventory
| Item | Qty | Weight | Details |
| ----------------------------------------------------------------------- | --- | ---------- | ----------------------------------------- |
| [Javelin](../../Equipment/Equipment_Javelin.md) | 5 | 2 lb. each | Simple Thrown Weapon, Slow Mastery |
| [Holy Symbol](../../Equipment/Equipment_Holy%20Symbol.md) | 1 | 1 lb. | Spellcasting Focus |
| [Pan Flute](../../Equipment/Equipment_Pan%20Flute.md) | 1 | 2 lb. | Musical Instrument (Species tool) |
| [Explorer's Pack](../../Equipment/Equipment_Explorer's%20Pack.md) | 1 | 19 lb. | Backpack and adventuring supplies |
| [Gaming Set / Instrument](../../Equipment/Equipment_Gaming%20Set.md) | 1 | — | Background tool of choice |
| [Scroll Case](../../Equipment/Equipment_Scroll%20Case.md) | 1 | 1 lb. | Letters of introduction from planar power |
| [Cosmic Token](../../Equipment/Equipment_Cosmic%20Token.md) | 1 | — | Planar keepsake (Background) |
| [Traveler's Clothes](../../Equipment/Equipment_Traveler's%20Clothes.md) | 1 | 4 lb. | Wearable clothes |

### 🪙 Currency
- **Copper (CP):** 0
- **Silver (SP):** 0
- **Electrum (EP):** 0
- **Gold (GP):** 15
- **Platinum (PP):** 0

---

## 📜 Character Backstory & Notes

### 🎭 Appearance
A dashing Satyr with sleek ram horns, clad in polished plate armor adorned with small silver ivy leaf emblems. He possesses a warm, charming smile and carries a well-crafted wooden pan flute at his belt. His shield is painted with a silver sunburst surrounded by grapevines, symbolizing both his devotion and his fey heritage.

### 🌟 Personality
Valiant, gregarious, and deeply joyful. Valerius believes that justice should be upheld with a song and a smile, and that protecting the weak is the highest and most noble form of performance. He is quick to offer a tune to cheer up a weary traveler, but just as quick to draw his moon-touched longsword if evildoers threaten the innocent.

### 🤝 Allies & Organizations
- **The Gilded Ivy Troupe:** A traveling band of bards, actors, and acrobats who took Valerius in when he first arrived in the Material Plane. They remain close friends, and he frequently performs with them when their paths cross.
- **The Order of the Gilded Leaf:** A small, localized order of Paladins and Rangers dedicated to protecting border towns and trade roads from fey incursions and monstrous threats. They value both chivalry and harmony with nature.

### 📖 Backstory (Planar Envoy)
Born in the vibrant, shifting groves of the Feywild, Valerius was chosen early by the Court of the Archfey to serve as a diplomat and messenger—a **Planar Envoy**. Armed with letters of introduction and a glowing cosmic token, he traveled the planes, negotiating borders between the Seelie Court and various planar lords, walking the portals of Sigil, and speaking with celestial archons.

These journeys exposed him to the fragility of the Material Plane and the heavy toll of planar incursions. Inspired by the legends of mortal knights who swore oaths to protect the weak, he knelt before an altar of the morning sun and took the **Oath of Devotion**. As an emissary to the Material Plane, he now travels the land, carrying out his diplomatic duties while defending the innocent with his shield, song, and moon-touched blade.
