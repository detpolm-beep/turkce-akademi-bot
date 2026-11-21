@echo off
chcp 65001 >nul
title Turkce Akademi Bot

echo.
echo ========================================
echo   TURKCE AKADEMI BOT - O'RNATISH
echo ========================================
echo.

:: Python tekshirish
python --version >nul 2>&1
if errorlevel 1 (
    echo [XATO] Python topilmadi!
    echo Python o'rnating: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python topildi

:: Kutubxona o'rnatish
echo.
echo [*] python-telegram-bot o'rnatilmoqda...
pip install python-telegram-bot==20.7 --quiet

if errorlevel 1 (
    echo [XATO] O'rnatishda xatolik!
    pause
    exit /b 1
)

echo [OK] Kutubxona o'rnatildi!
echo.
echo ========================================
echo   BOT ISHGA TUSHMOQDA...
echo ========================================
echo.
echo Telegram'da botingizni oching va /start yuboring!
echo.
echo To'xtatish uchun bu oynani yoping yoki Ctrl+C bosing
echo.

python bot.py

pause
