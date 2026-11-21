#!/usr/bin/env python3
# ============================================================
#  Türkçe Akademi – Kengaytirilgan Telegram Bot v2.0
# ============================================================

import logging, json, os, random
from datetime import date
import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from data import (
    FLASHCARDS, DAILY_WORDS, QUIZ_QUESTIONS, GRAMMAR_LESSONS,
    DIALOGUES, LEVELS, BADGES, TOPICS, TOPIC_WORDS,
    ADJECTIVES, PRONUNCIATION_GUIDE, HELP_PHRASES
)

import os
TOKEN = os.environ.get("BOT_TOKEN", "9184512017:AAEWCl08bm15sTjCMcLRzPsVNRE9LOTUvLc")
DB_FILE = "users_db.json"

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# ── DB ────────────────────────────────────────────────────
def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def get_user(uid):
    db = load_db()
    k = str(uid)
    if k not in db:
        db[k] = {
            "xp": 0, "level": 0, "quiz_correct": 0, "quiz_total": 0,
            "daily_day": 0, "daily_last": "", "grammar_done": [],
            "flashcard_seen": 0, "badges": [], "streak": 0,
            "last_activity": str(date.today()), "favorites": [],
            "joined": str(date.today()), "topics_done": [],
        }
        save_db(db)
    return db[k]

def update_user(uid, data):
    db = load_db(); db[str(uid)].update(data); save_db(db)

def add_xp(uid, xp):
    u = get_user(uid); new = u["xp"] + xp
    lvl = max(i for i, l in enumerate(LEVELS) if new >= l["min_xp"])
    update_user(uid, {"xp": new, "level": lvl})
    # XP badge
    if new >= 500: check_badge(uid, "xp_500")
    if new >= 1000: check_badge(uid, "xp_1000")
    return new, lvl

def check_badge(uid, bid):
    u = get_user(uid)
    if bid not in u["badges"]:
        u["badges"].append(bid); update_user(uid, {"badges": u["badges"]})
        for b in BADGES:
            if b["id"] == bid: return b
    return None

def get_level_info(xp):
    cur = LEVELS[0]
    for l in LEVELS:
        if xp >= l["min_xp"]: cur = l
    return cur

# ── MENU ─────────────────────────────────────────────────
def main_menu_kb():
    return ReplyKeyboardMarkup([
        [KeyboardButton("🃏 Flashcards"), KeyboardButton("📝 Quiz")],
        [KeyboardButton("📅 Kunlik So'zlar"), KeyboardButton("📚 Grammatika")],
        [KeyboardButton("🗂️ Mavzular"), KeyboardButton("🎨 Sifatlar")],
        [KeyboardButton("🗣️ Real Life"), KeyboardButton("🎧 Listening")],
        [KeyboardButton("🔤 Talaffuz"), KeyboardButton("🆘 Yordam Iboralari")],
        [KeyboardButton("⭐ Darajam"), KeyboardButton("🏆 Reyting")],
        [KeyboardButton("❤️ Sevimlilar"), KeyboardButton("ℹ️ Info")],
    ], resize_keyboard=True)

# ── START ─────────────────────────────────────────────────
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user; get_user(u.id)
    await update.message.reply_text(
        f"🇹🇷 *Türkçe Akademi'ye Hoş Geldiniz!*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👋 Assalomu alaykum, *{u.first_name}*!\n\n"
        f"Men *Türkçe Akademi* botiman 🤖\n"
        f"Sizga turk tilini 0 dan o'rgataman! 🚀\n\n"
        f"*Nima o'rganasiz?*\n"
        f"🃏 Flashcards │ 📝 Quiz\n"
        f"📅 Kunlik So'zlar │ 📚 Grammatika\n"
        f"🗂️ Mavzular (24 ta!) │ 🎨 Sifatlar (200+)\n"
        f"🗣️ Real Life │ 🎧 Listening\n"
        f"🔤 Talaffuz │ 🆘 Yordam Iboralari\n\n"
        f"👇 Pastdagi tugmalardan birini tanlang!",
        parse_mode="Markdown", reply_markup=main_menu_kb()
    )

# ── FLASHCARDS ────────────────────────────────────────────
async def flashcards_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    card = random.choice(FLASHCARDS); ctx.user_data["current_card"] = card
    u = get_user(uid); seen = u.get("flashcard_seen", 0) + 1
    update_user(uid, {"flashcard_seen": seen})
    if seen >= 20: check_badge(uid, "flashcard_20")
    kb = [[InlineKeyboardButton("👁️ Tarjimasini ko'r", callback_data="flash_show")],
          [InlineKeyboardButton("❤️ Saqlash", callback_data="flash_save"),
           InlineKeyboardButton("➡️ Keyingi", callback_data="flash_next")],
          [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    txt = f"🃏 *FLASHCARD* (#{seen})\n━━━━━━━━━━━━━━━━━━━━━━\n\n{card['emoji']} *{card['tr']}*\n\n❓ Tarjimasi qanday?\n\n👆 Ko'rish uchun tugmani bosing"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def flash_show(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    card = ctx.user_data.get("current_card", random.choice(FLASHCARDS))
    add_xp(q.from_user.id, 2)
    kb = [[InlineKeyboardButton("❤️ Saqlash", callback_data="flash_save"),
           InlineKeyboardButton("➡️ Keyingi", callback_data="flash_next")],
          [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    await q.edit_message_text(
        f"🃏 *FLASHCARD – JAVOB*\n━━━━━━━━━━━━━━━━━━━━━━\n\n{card['emoji']} *{card['tr']}*\n📌 *O'zbekcha:* {card['uz']}\n\n✅ +2 XP qo'shildi!",
        parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def flash_next(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer(); await flashcards_menu(update, ctx)

async def flash_save(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer("❤️ Saqlandi!")
    card = ctx.user_data.get("current_card")
    if card:
        u = get_user(q.from_user.id); favs = u.get("favorites", [])
        if card["tr"] not in [f.get("tr") for f in favs]:
            favs.append(card); update_user(q.from_user.id, {"favorites": favs})

# ── QUIZ ──────────────────────────────────────────────────
async def quiz_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    questions = random.sample(QUIZ_QUESTIONS, min(10, len(QUIZ_QUESTIONS)))
    ctx.user_data.update({"quiz_questions": questions, "quiz_index": 0, "quiz_score": 0, "quiz_wrong": []})
    kb = [[InlineKeyboardButton("🚀 Boshlash!", callback_data="quiz_start")]]
    txt = "📝 *QUIZ*\n━━━━━━━━━━━━━━━━━━━━━━\n\n📊 10 ta savol\n⭐ Har to'g'ri javob: +10 XP\n\nTayyor? 🚀"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def quiz_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer(); await send_quiz_q(update, ctx)

async def send_quiz_q(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    questions = ctx.user_data.get("quiz_questions", []); idx = ctx.user_data.get("quiz_index", 0)
    if idx >= len(questions): await quiz_finish(update, ctx); return
    qi = questions[idx]
    kb = [[InlineKeyboardButton(f"{'ABCD'[i]}. {o}", callback_data=f"quiz_ans_{i}")] for i, o in enumerate(qi["options"])]
    await q.edit_message_text(
        f"📝 *SAVOL {idx+1}/10*\n━━━━━━━━━━━━━━━━━━━━━━\n\n{qi['question']}\n\n👇 To'g'ri javobni tanlang:",
        parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def quiz_answer(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    ans = int(q.data.split("_")[-1])
    questions = ctx.user_data.get("quiz_questions", []); idx = ctx.user_data.get("quiz_index", 0)
    score = ctx.user_data.get("quiz_score", 0); qi = questions[idx]
    if ans == qi["correct"]:
        score += 1; ctx.user_data["quiz_score"] = score; add_xp(q.from_user.id, 10)
        txt = f"✅ *TO'G'RI!* +10 XP\n━━━━━━━━━━━━━━━━━━━━━━\n{qi['explanation']}"
    else:
        w = ctx.user_data.get("quiz_wrong", [])
        w.append({"wrong": qi["options"][ans], "correct": qi["options"][qi["correct"]]})
        ctx.user_data["quiz_wrong"] = w
        txt = f"❌ *XATO!*\n━━━━━━━━━━━━━━━━━━━━━━\nSiz: {qi['options'][ans]}\nTo'g'ri: *{qi['options'][qi['correct']]}*\n\n{qi['explanation']}"
    ctx.user_data["quiz_index"] = idx + 1
    await q.edit_message_text(txt, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ Keyingi", callback_data="quiz_next")]]))

async def quiz_next(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer(); await send_quiz_q(update, ctx)

async def quiz_finish(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; uid = q.from_user.id
    score = ctx.user_data.get("quiz_score", 0); wrong = ctx.user_data.get("quiz_wrong", [])
    u = get_user(uid); tc = u["quiz_correct"] + score; tt = u["quiz_total"] + 10
    update_user(uid, {"quiz_correct": tc, "quiz_total": tt})
    badge_msg = ""
    for bid, threshold in [("first_quiz", 1), ("quiz_10", 10), ("quiz_50", 50)]:
        if tc >= threshold:
            b = check_badge(uid, bid)
            if b: badge_msg = f"\n\n🎉 *Yangi yutuq: {b['name']}!*"
    em = "🏆" if score >= 8 else "⭐" if score >= 5 else "📚"
    txt = f"{em} *QUIZ YAKUNLANDI!*\n━━━━━━━━━━━━━━━━━━━━━━\n\n📊 Natija: *{score}/10*\n⭐ XP: *+{score*10}*\n📈 Jami to'g'ri: {tc}"
    if wrong:
        txt += "\n\n❌ *Xato qilinganlar:*"
        for w in wrong[:3]: txt += f"\n• {w['wrong']} → {w['correct']}"
    txt += badge_msg
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Yana", callback_data="quiz_menu")],
        [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]))

# ── KUNLIK SO'ZLAR ────────────────────────────────────────
async def daily_words(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id; u = get_user(uid)
    today = str(date.today()); day_i = u.get("daily_day", 0) % len(DAILY_WORDS)
    words = DAILY_WORDS[day_i]; already = u.get("daily_last") == today
    txt = f"📅 *KUNLIK 10 TA SO'Z*\n━━━━━━━━━━━━━━━━━━━━━━\n📆 Kun #{day_i+1} | {today}\n\n"
    for i, w in enumerate(words, 1):
        txt += f"*{i}.* 🇹🇷 {w['tr']} → 🇺🇿 {w['uz']}\n   _{w['example']}_\n\n"
    if not already:
        add_xp(uid, 20); update_user(uid, {"daily_day": u.get("daily_day",0)+1, "daily_last": today})
        txt += "✅ *+20 XP* qo'shildi!"
        b = check_badge(uid, "daily_1")
        if b: txt += f"\n\n🎉 *{b['name']}!*"
    else:
        txt += "✅ Bugun allaqachon o'rgandingiz!"
    kb = [[InlineKeyboardButton("➡️ Keyingi kun", callback_data="daily_next")],
          [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def daily_next(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer(); uid = q.from_user.id
    u = get_user(uid); update_user(uid, {"daily_day": (u.get("daily_day",0)+1) % len(DAILY_WORDS)})
    await daily_words(update, ctx)

# ── GRAMMATIKA ────────────────────────────────────────────
async def grammar_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = get_user(update.effective_user.id); done = u.get("grammar_done", [])
    kb = [[InlineKeyboardButton(
        f"{'✅' if i in done else '📖'} {l['title'].split(': ',1)[-1][:35]}",
        callback_data=f"gram_{i}")] for i, l in enumerate(GRAMMAR_LESSONS)]
    kb.append([InlineKeyboardButton("🔙 Menu", callback_data="main_menu")])
    txt = f"📚 *GRAMMATIKA DARSLARI*\n━━━━━━━━━━━━━━━━━━━━━━\n✅ Tugatilgan: {len(done)}/{len(GRAMMAR_LESSONS)}\n\nDarsni tanlang:"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def grammar_lesson(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    idx = int(q.data.split("_")[1]); lesson = GRAMMAR_LESSONS[idx]; uid = q.from_user.id
    u = get_user(uid); done = u.get("grammar_done", [])
    if idx not in done:
        done.append(idx); update_user(uid, {"grammar_done": done}); add_xp(uid, 15)
        b = check_badge(uid, "grammar_1")
        xp_msg = f"\n\n✅ *+15 XP!*{' 🎉 '+b['name'] if b else ''}"
    else:
        xp_msg = ""
    nav = []
    if idx > 0: nav.append(InlineKeyboardButton("⬅️ Oldingi", callback_data=f"gram_{idx-1}"))
    if idx < len(GRAMMAR_LESSONS)-1: nav.append(InlineKeyboardButton("➡️ Keyingi", callback_data=f"gram_{idx+1}"))
    rows = [nav] if nav else []
    rows += [[InlineKeyboardButton("📋 Darslar", callback_data="grammar_menu")],
             [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    await q.edit_message_text(lesson["content"] + xp_msg, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(rows))

# ── MAVZULAR ─────────────────────────────────────────────
async def topics_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    keys = list(TOPICS.keys())
    kb = []
    for i in range(0, len(keys), 2):
        row = [InlineKeyboardButton(TOPICS[keys[i]], callback_data=f"topic_{keys[i]}")]
        if i+1 < len(keys):
            row.append(InlineKeyboardButton(TOPICS[keys[i+1]], callback_data=f"topic_{keys[i+1]}"))
        kb.append(row)
    kb.append([InlineKeyboardButton("🔙 Menu", callback_data="main_menu")])
    txt = "🗂️ *MAVZULAR (Topics)*\n━━━━━━━━━━━━━━━━━━━━━━\nQiziqtirgan mavzuni tanlang:"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def show_topic(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    parts = q.data.split("_", 1); key = parts[1] if len(parts) > 1 else ""
    # Pagination
    page = 0
    if "_p" in key:
        key, p = key.rsplit("_p", 1); page = int(p)
    words = TOPIC_WORDS.get(key, [])
    per_page = 10; total_pages = (len(words) - 1) // per_page + 1
    chunk = words[page*per_page:(page+1)*per_page]
    title = TOPICS.get(key, key)
    txt = f"🗂️ *{title}*\n━━━━━━━━━━━━━━━━━━━━━━\n📖 {page*per_page+1}-{min((page+1)*per_page, len(words))} / {len(words)} ta so'z\n\n"
    for i, w in enumerate(chunk, page*per_page+1):
        example = w.get("example", "")
        txt += f"*{i}.* 🇹🇷 *{w['tr']}* → 🇺🇿 {w['uz']}\n"
        if example: txt += f"   _{example}_\n"
    add_xp(q.from_user.id, 5)
    b = check_badge(q.from_user.id, "topic_1")
    if b: txt += f"\n\n🎉 *{b['name']}!*"
    nav = []
    if page > 0: nav.append(InlineKeyboardButton("⬅️", callback_data=f"topic_{key}_p{page-1}"))
    nav.append(InlineKeyboardButton(f"{page+1}/{total_pages}", callback_data="noop"))
    if page < total_pages - 1: nav.append(InlineKeyboardButton("➡️", callback_data=f"topic_{key}_p{page+1}"))
    kb = [nav, [InlineKeyboardButton("🗂️ Mavzular", callback_data="topics_menu")],
          [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── SIFATLAR ─────────────────────────────────────────────
async def adjectives_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    # Kategoriyalar
    cats = {}
    for a in ADJECTIVES:
        c = a.get("category", "boshqa")
        if c not in cats: cats[c] = []
        cats[c].append(a)
    cat_names = {
        "o'lcham": "📏 O'lcham", "korinish": "👁️ Ko'rinish",
        "hissiyot": "😊 Hissiyot", "xarakter": "💬 Xarakter",
        "holat": "🏃 Holat", "muhit": "🌤️ Muhit",
        "narsa": "📦 Narsa/Sifat", "rang": "🌈 Rang",
        "miqdor": "📊 Miqdor",
    }
    kb = [[InlineKeyboardButton(cat_names.get(c, c) + f" ({len(v)})", callback_data=f"adj_{c}")] for c, v in cats.items()]
    kb.append([InlineKeyboardButton("🎲 Tasodifiy sifat", callback_data="adj_random")])
    kb.append([InlineKeyboardButton("🔙 Menu", callback_data="main_menu")])
    txt = f"🎨 *SIFATLAR (Adjectives)*\n━━━━━━━━━━━━━━━━━━━━━━\nJami: {len(ADJECTIVES)} ta sifat!\n\nKategoriyani tanlang:"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def show_adjectives(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    parts = q.data.split("_", 1); cat_key = parts[1] if len(parts) > 1 else ""
    page = 0
    if "_p" in cat_key:
        cat_key, p = cat_key.rsplit("_p", 1); page = int(p)
    if cat_key == "random":
        adj = random.choice(ADJECTIVES)
        txt = (f"🎲 *TASODIFIY SIFAT*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
               f"🇹🇷 *{adj['tr']}*\n🇺🇿 {adj['uz']}\n📝 _{adj.get('example','')}_")
        add_xp(q.from_user.id, 2)
        kb = [[InlineKeyboardButton("🎲 Yana tasodifiy", callback_data="adj_random")],
              [InlineKeyboardButton("🔙 Sifatlar", callback_data="adjectives_menu")]]
        await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb)); return
    words = [a for a in ADJECTIVES if a.get("category") == cat_key]
    per_page = 10; total_pages = max(1, (len(words)-1)//per_page+1)
    chunk = words[page*per_page:(page+1)*per_page]
    cat_names = {
        "o'lcham": "📏 O'lcham", "korinish": "👁️ Ko'rinish",
        "hissiyot": "😊 Hissiyot", "xarakter": "💬 Xarakter",
        "holat": "🏃 Holat", "muhit": "🌤️ Muhit",
        "narsa": "📦 Narsa/Sifat", "rang": "🌈 Rang", "miqdor": "📊 Miqdor",
    }
    title = cat_names.get(cat_key, cat_key)
    txt = f"🎨 *{title} SIFATLARI*\n━━━━━━━━━━━━━━━━━━━━━━\n📖 {page*per_page+1}-{min((page+1)*per_page,len(words))}/{len(words)}\n\n"
    for w in chunk:
        txt += f"🇹🇷 *{w['tr']}* → 🇺🇿 {w['uz']}\n   _{w.get('example','')}_\n\n"
    add_xp(q.from_user.id, 3); check_badge(q.from_user.id, "adjective_1")
    nav = []
    if page > 0: nav.append(InlineKeyboardButton("⬅️", callback_data=f"adj_{cat_key}_p{page-1}"))
    nav.append(InlineKeyboardButton(f"{page+1}/{total_pages}", callback_data="noop"))
    if page < total_pages-1: nav.append(InlineKeyboardButton("➡️", callback_data=f"adj_{cat_key}_p{page+1}"))
    kb = [nav, [InlineKeyboardButton("🔙 Sifatlar", callback_data="adjectives_menu")]]
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── REAL LIFE ─────────────────────────────────────────────
async def reallife_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton(d["title"], callback_data=f"dlg_{i}")] for i, d in enumerate(DIALOGUES)]
    kb.append([InlineKeyboardButton("🔙 Menu", callback_data="main_menu")])
    txt = "🗣️ *REAL LIFE TURKISH*\n━━━━━━━━━━━━━━━━━━━━━━\nMavzuni tanlang:"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def show_dialogue(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    idx = int(q.data.split("_")[1]); dlg = DIALOGUES[idx]
    add_xp(q.from_user.id, 5)
    txt = f"{dlg['title']}\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for line in dlg["lines"]:
        txt += f"*{line['speaker']}:*\n🇹🇷 _{line['tr']}_\n🇺🇿 {line['uz']}\n\n"
    txt += "✅ *+5 XP* qo'shildi!"
    kb = [[InlineKeyboardButton("🔙 Dialoglar", callback_data="reallife_menu")],
          [InlineKeyboardButton("🏠 Menu", callback_data="main_menu")]]
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── LISTENING ─────────────────────────────────────────────
async def listening_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    words = random.sample(FLASHCARDS, 5)
    ctx.user_data.update({"listen_words": words, "listen_index": 0, "listen_score": 0})
    kb = [[InlineKeyboardButton("🎧 Boshlash!", callback_data="listen_start")]]
    txt = "🎧 *LISTENING*\n━━━━━━━━━━━━━━━━━━━━━━\n📌 O'zbekcha ko'ring → Turkcha toping!\n5 ta savol | Har to'g'ri: +8 XP"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def listen_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer(); await send_listen_q(update, ctx)

async def send_listen_q(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    words = ctx.user_data.get("listen_words", []); idx = ctx.user_data.get("listen_index", 0)
    if idx >= len(words): await listen_finish(update, ctx); return
    cw = words[idx]
    wrong = random.sample([w for w in FLASHCARDS if w["tr"] != cw["tr"]], 3)
    opts = wrong + [cw]; random.shuffle(opts)
    ci = opts.index(cw); ctx.user_data.update({"listen_correct": ci, "listen_options": opts})
    kb = [[InlineKeyboardButton(f"{'ABCD'[i]}. {o['tr']}", callback_data=f"listen_ans_{i}")] for i, o in enumerate(opts)]
    await q.edit_message_text(
        f"🎧 *LISTENING {idx+1}/5*\n━━━━━━━━━━━━━━━━━━━━━━\n🇺🇿 *{cw['uz']}*\n\nTurkchasi qaysi? 👇",
        parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def listen_answer(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    ans = int(q.data.split("_")[-1]); correct = ctx.user_data.get("listen_correct", 0)
    opts = ctx.user_data.get("listen_options", []); score = ctx.user_data.get("listen_score", 0)
    idx = ctx.user_data.get("listen_index", 0)
    if ans == correct:
        score += 1; ctx.user_data["listen_score"] = score; add_xp(q.from_user.id, 8); result = "✅ *TO'G'RI!* +8 XP"
    else:
        result = f"❌ *XATO!*\nTo'g'ri: *{opts[correct]['tr']}* = {opts[correct]['uz']}"
    ctx.user_data["listen_index"] = idx + 1
    await q.edit_message_text(result, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡️ Keyingi", callback_data="listen_next")]]))

async def listen_next(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer(); await send_listen_q(update, ctx)

async def listen_finish(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; score = ctx.user_data.get("listen_score", 0)
    em = "🏆" if score==5 else "⭐" if score>=3 else "📚"
    await q.edit_message_text(
        f"🎧 *LISTENING YAKUNLANDI!*\n━━━━━━━━━━━━━━━━━━━━━━\n📊 {score}/5\n⭐ +{score*8} XP\n{em}",
        parse_mode="Markdown", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔄 Yana", callback_data="listening_menu")],
            [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]))

# ── TALAFFUZ ─────────────────────────────────────────────
async def pronunciation_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("🔤 Harflar va talaffuz", callback_data="pron_harflar")],
        [InlineKeyboardButton("📋 Muhim qoidalar", callback_data="pron_qoidalar")],
        [InlineKeyboardButton("🗣️ Talaffuz misollari", callback_data="pron_misollar")],
        [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")],
    ]
    txt = "🔤 *TALAFFUZ O'RGANISH*\n━━━━━━━━━━━━━━━━━━━━━━\nTurkcha talaffuzni to'g'ri o'rganing!\n\nBo'limni tanlang:"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def pron_harflar(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    page = int(q.data.split("_p")[1]) if "_p" in q.data else 0
    harflar = PRONUNCIATION_GUIDE["harflar"]; per = 8
    total = (len(harflar)-1)//per+1; chunk = harflar[page*per:(page+1)*per]
    txt = f"🔤 *TURKCHA HARFLAR* ({page*per+1}-{min((page+1)*per,len(harflar))})\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for h in chunk:
        txt += f"*{h['harf']}* → {h['talaffuz']}\n📝 _{h['misol']}_\n\n"
    add_xp(q.from_user.id, 3); check_badge(q.from_user.id, "pronounce_1")
    nav = []
    if page > 0: nav.append(InlineKeyboardButton("⬅️", callback_data=f"pron_harflar_p{page-1}"))
    nav.append(InlineKeyboardButton(f"{page+1}/{total}", callback_data="noop"))
    if page < total-1: nav.append(InlineKeyboardButton("➡️", callback_data=f"pron_harflar_p{page+1}"))
    kb = [nav, [InlineKeyboardButton("🔙 Talaffuz", callback_data="pronunciation_menu")]]
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def pron_qoidalar(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    qoidalar = PRONUNCIATION_GUIDE["qoidalar"]
    txt = "📋 *MUHIM TALAFFUZ QOIDALARI*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for i, qoida in enumerate(qoidalar, 1): txt += f"{i}. {qoida}\n"
    add_xp(q.from_user.id, 5)
    kb = [[InlineKeyboardButton("🔙 Talaffuz", callback_data="pronunciation_menu")],
          [InlineKeyboardButton("🏠 Menu", callback_data="main_menu")]]
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def pron_misollar(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    misollar = PRONUNCIATION_GUIDE["misollar"]
    txt = "🗣️ *TALAFFUZ MISOLLARI*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for m in misollar:
        txt += (f"🇹🇷 *{m['tr']}*\n🇺🇿 {m['uz']}\n"
                f"🔊 *O'qilishi:* `{m['pronounce']}`\n"
                f"💡 _{m['tip']}_\n\n")
    add_xp(q.from_user.id, 5)
    kb = [[InlineKeyboardButton("🔙 Talaffuz", callback_data="pronunciation_menu")]]
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── HELP IBORALAR ─────────────────────────────────────────
async def help_phrases_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    sections = {
        "tushunmadim": "🤷 Tushunmadim",
        "yozish": "✍️ Yozish",
        "yordam": "🆘 Yordam",
        "dokon": "🛒 Do'konda",
        "restoran": "🍽️ Restoranda",
    }
    kb = [[InlineKeyboardButton(v, callback_data=f"helph_{k}")] for k, v in sections.items()]
    kb.append([InlineKeyboardButton("🔙 Menu", callback_data="main_menu")])
    txt = "🆘 *YORDAM IBORALARI*\n━━━━━━━━━━━━━━━━━━━━━━\nTurkiyada kerak bo'ladigan iboralar!\n\nMavzuni tanlang:"
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def show_help_phrases(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    key = q.data.split("_", 1)[1]
    phrases = HELP_PHRASES.get(key, [])
    sec_names = {
        "tushunmadim": "🤷 Tushunmadim / Tushuntiring",
        "yozish": "✍️ Yozib berish",
        "yordam": "🆘 Yordam so'rash",
        "dokon": "🛒 Do'konda",
        "restoran": "🍽️ Restoranda",
    }
    txt = f"{sec_names.get(key, key)}\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for p in phrases:
        txt += f"🇹🇷 *{p['tr']}*\n🇺🇿 _{p['uz']}_\n💡 {p.get('use','')}\n\n"
    add_xp(q.from_user.id, 3); check_badge(q.from_user.id, "help_1")
    kb = [[InlineKeyboardButton("🔙 Yordam iboralari", callback_data="help_phrases")],
          [InlineKeyboardButton("🏠 Menu", callback_data="main_menu")]]
    await q.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── DARAJAM ───────────────────────────────────────────────
async def my_level(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id; u = get_user(uid)
    xp = u["xp"]; li = get_level_info(xp)
    nxt = next((l for l in LEVELS if l["min_xp"] > xp), None)
    if nxt:
        prog = xp - li["min_xp"]; tot = nxt["min_xp"] - li["min_xp"]
        bars = int((prog/tot)*10); pb = "█"*bars + "░"*(10-bars)
        pbar = f"\n📊 [{pb}] {nxt['min_xp']-xp} XP qoldi"
    else:
        pbar = "\n🏆 Maksimal daraja!"
    badges = u.get("badges", []); badge_txt = ""
    if badges:
        badge_txt = "\n\n🏅 *Yutuqlarim:*\n"
        for bid in badges:
            for b in BADGES:
                if b["id"] == bid: badge_txt += f"  {b['name']} – {b['desc']}\n"
    acc = int(u["quiz_correct"]/u["quiz_total"]*100) if u["quiz_total"] > 0 else 0
    txt = (f"⭐ *MENING DARAJAM*\n━━━━━━━━━━━━━━━━━━━━━━\n"
           f"🎖️ *{li['name']}*\n✨ XP: *{xp}*{pbar}\n\n"
           f"📊 *Statistika:*\n"
           f"📝 Testlar: {u['quiz_total']} ({acc}% to'g'ri)\n"
           f"🃏 Flashcard: {u['flashcard_seen']} ta\n"
           f"📚 Grammatika: {len(u['grammar_done'])}/{len(GRAMMAR_LESSONS)}\n"
           f"📅 Kunlik: {u['daily_day']} kun\n"
           f"🏅 Yutuqlar: {len(badges)} ta{badge_txt}")
    kb = [[InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── REYTING ───────────────────────────────────────────────
async def leaderboard(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    db = load_db(); srt = sorted(db.items(), key=lambda x: x[1].get("xp",0), reverse=True)
    medals = ["🥇","🥈","🥉","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    txt = "🏆 *TOP REYTING*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for i, (uid, ud) in enumerate(srt[:10]):
        li = get_level_info(ud.get("xp",0)); m = medals[i] if i<len(medals) else f"{i+1}."
        txt += f"{m} *{ud.get('xp',0)} XP* – {li['name']}\n"
    if not srt: txt += "_Hali hech kim yo'q_"
    kb = [[InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── SEVIMLILAR ────────────────────────────────────────────
async def favorites(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id; u = get_user(uid); favs = u.get("favorites", [])
    if not favs:
        txt = "❤️ *SEVIMLILAR*\n━━━━━━━━━━━━━━━━━━━━━━\nHali saqlangan so'z yo'q.\n\nFlashcards'da ❤️ Saqlash tugmasini bosing!"
    else:
        txt = f"❤️ *SEVIMLILAR* ({len(favs)} ta)\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
        for w in favs: txt += f"{w['emoji']} *{w['tr']}* → {w['uz']}\n"
    kb = [[InlineKeyboardButton("🗑️ Tozalash", callback_data="favs_clear")],
          [InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

async def favs_clear(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer("🗑️ Tozalandi!")
    update_user(q.from_user.id, {"favorites": []})
    await q.edit_message_text("❤️ *SEVIMLILAR*\n\n✅ Ro'yxat tozalandi!",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]))

# ── INFO ──────────────────────────────────────────────────
async def info_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    txt = ("ℹ️ *TÜRKÇE AKADEMİ*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
           "📌 *Buyruqlar:*\n/start – Qayta boshlash\n/stats – Statistika\n/top – Reyting\n\n"
           "📚 *Bo'limlar:*\n"
           "🃏 Flashcards – 90+ kartochka\n"
           "📝 Quiz – 40+ savol\n"
           "📅 Kunlik – 10 ta kunlik so'z\n"
           "📚 Grammatika – 12 ta dars\n"
           "🗂️ Mavzular – 24 ta mavzu\n"
           "🎨 Sifatlar – 200+ sifat (9 kategoriya)\n"
           "🗣️ Real Life – 10 ta dialog\n"
           "🎧 Listening – tinglash testi\n"
           "🔤 Talaffuz – harflar, qoidalar\n"
           "🆘 Yordam Iboralari – 5 ta mavzu\n\n"
           "⭐ *XP Tizimi:*\n"
           "🃏 Flashcard: +2 │ 📝 Quiz: +10\n"
           "📅 Kunlik: +20 │ 📚 Grammar: +15\n"
           "🗂️ Mavzu: +5 │ 🎨 Sifat: +3\n"
           "🗣️ Dialog: +5 │ 🎧 Listening: +8\n"
           "🔤 Talaffuz: +3-5")
    kb = [[InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]]
    if update.callback_query:
        await update.callback_query.edit_message_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))
    else:
        await update.message.reply_text(txt, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(kb))

# ── MATN XABARLARI ────────────────────────────────────────
async def handle_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    t = update.message.text
    routes = {
        "🃏 Flashcards": flashcards_menu,
        "📝 Quiz": quiz_menu,
        "📅 Kunlik So'zlar": daily_words,
        "📚 Grammatika": grammar_menu,
        "🗂️ Mavzular": topics_menu,
        "🎨 Sifatlar": adjectives_menu,
        "🗣️ Real Life": reallife_menu,
        "🎧 Listening": listening_menu,
        "🔤 Talaffuz": pronunciation_menu,
        "🆘 Yordam Iboralari": help_phrases_menu,
        "⭐ Darajam": my_level,
        "🏆 Reyting": leaderboard,
        "❤️ Sevimlilar": favorites,
        "ℹ️ Info": info_menu,
    }
    if t in routes:
        await routes[t](update, ctx)
    else:
        await update.message.reply_text(
            "❓ Nima demoqchi ekaningizni tushunmadim.\nPastdagi tugmalardan birini tanlang 👇",
            reply_markup=main_menu_kb())

# ── CALLBACK ──────────────────────────────────────────────
async def handle_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; d = q.data
    if d == "noop": await q.answer(); return
    if d == "main_menu":
        await q.answer()
        await q.message.reply_text("🏠 *Asosiy menyu*", parse_mode="Markdown", reply_markup=main_menu_kb())
    elif d == "flash_show": await flash_show(update, ctx)
    elif d == "flash_next": await flash_next(update, ctx)
    elif d == "flash_save": await flash_save(update, ctx)
    elif d == "quiz_menu": await quiz_menu(update, ctx)
    elif d == "quiz_start": await quiz_start(update, ctx)
    elif d.startswith("quiz_ans_"): await quiz_answer(update, ctx)
    elif d == "quiz_next": await quiz_next(update, ctx)
    elif d == "daily_next": await daily_next(update, ctx)
    elif d == "grammar_menu": await grammar_menu(update, ctx)
    elif d.startswith("gram_"): await grammar_lesson(update, ctx)
    elif d == "topics_menu": await topics_menu(update, ctx)
    elif d.startswith("topic_"): await show_topic(update, ctx)
    elif d == "adjectives_menu": await adjectives_menu(update, ctx)
    elif d.startswith("adj_"): await show_adjectives(update, ctx)
    elif d == "reallife_menu": await reallife_menu(update, ctx)
    elif d.startswith("dlg_"): await show_dialogue(update, ctx)
    elif d == "listening_menu": await listening_menu(update, ctx)
    elif d == "listen_start": await listen_start(update, ctx)
    elif d.startswith("listen_ans_"): await listen_answer(update, ctx)
    elif d == "listen_next": await listen_next(update, ctx)
    elif d == "pronunciation_menu": await pronunciation_menu(update, ctx)
    elif d == "pron_qoidalar": await pron_qoidalar(update, ctx)
    elif d == "pron_misollar": await pron_misollar(update, ctx)
    elif d.startswith("pron_harflar"): await pron_harflar(update, ctx)
    elif d == "help_phrases": await help_phrases_menu(update, ctx)
    elif d.startswith("helph_"): await show_help_phrases(update, ctx)
    elif d == "favs_clear": await favs_clear(update, ctx)

# ── MAIN ──────────────────────────────────────────────────
def main():
    print("🇹🇷 Türkçe Akademi v2.0 ishga tushmoqda...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", my_level))
    app.add_handler(CommandHandler("top", leaderboard))
    app.add_handler(CommandHandler("help", info_menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_callback))
    print("✅ Bot muvaffaqiyatli ishga tushdi! v2.0")
    print("📱 Telegram'da /start yuboring")
    print("⌨️ To'xtatish: Ctrl+C")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
