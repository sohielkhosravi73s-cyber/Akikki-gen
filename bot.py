from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8940330226:AAFfSRuDQS-Y_onyR99ig0w1s77LMi4JjBk"

# Genetik bilgi bankası
GENETIK_BILGI = {
    "dna": "DNA, genetik bilgiyi taşıyan çift sarmallı moleküldür.",
    "rna": "RNA, protein sentezinde görev alan tek zincirli moleküldür.",
    "gen": "Gen, kalıtsal özellikleri belirleyen DNA parçasıdır.",
    "mutasyon": "Mutasyon, DNA dizisinde meydana gelen kalıcı değişikliktir.",
    "kromozom": "Kromozom, DNA ve proteinlerden oluşan yapıdır.",
    "mitoz": "Mitoz, bir hücrenin iki aynı hücreye bölünmesidir.",
    "mayoz": "Mayoz, üreme hücrelerini oluşturan bölünme türüdür.",
    "genetik": "Genetik, kalıtım ve genleri inceleyen bilim dalıdır.",
    "protein": "Proteinler amino asitlerden oluşan hücresel yapılardır."
}

# Göz rengi tahmini
GOZ_RENKLERI = {
    ("mavi", "mavi"): "Çocuk büyük ihtimalle mavi gözlü olur.",
    ("kahverengi", "mavi"): "Çocuk büyük ihtimalle kahverengi gözlü olur.",
    ("mavi", "kahverengi"): "Çocuk büyük ihtimalle kahverengi gözlü olur.",
    ("yesil", "mavi"): "Çocuk yeşil veya mavi gözlü olabilir.",
    ("kahverengi", "yesil"): "Çocuk kahverengi veya yeşil gözlü olabilir."
}

# Saç rengi tahmini
SAC_RENKLERI = {
    ("sarisin", "sarisin"): "Çocuk büyük ihtimalle sarışın olur.",
    ("esmer", "sarisin"): "Çocuk kumral veya esmer olabilir.",
    ("kumral", "sarisin"): "Çocuk kumral olabilir."
}

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧬 Genetik Bot Aktif!\n"
        "Genetik sorularını sorabilirsin."
    )

# Mesaj cevaplama
async def cevapla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Göz rengi analizi
    for (a, b), sonuc in GOZ_RENKLERI.items():
        if a in text and b in text:
            await update.message.reply_text("👁️ " + sonuc)
            return

    # Saç rengi analizi
    for (a, b), sonuc in SAC_RENKLERI.items():
        if a in text and b in text:
            await update.message.reply_text("🧬 " + sonuc)
            return

    # Genetik bilgi
    for key, value in GENETIK_BILGI.items():
        if key in text:
            await update.message.reply_text(value)
            return

    await update.message.reply_text(
        "⚠️ Sadece genetik konularında yardımcı olabiliyorum."
    )

# Botu başlat
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, cevapla))

print("🧬 Genetik Bot çalışıyor...")
app.run_polling()