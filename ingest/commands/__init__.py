from telethon import events
from ingest.db import connect


def register_command_handlers(client):
    @client.on(events.NewMessage(pattern=r"^/help"))
    async def help_cmd(event):
        await event.reply("Commands: /help, /filtr <mcap> <liq>, /spikesedit <threshold> [sec]")

    @client.on(events.NewMessage(pattern=r"^/filtr\s+(\d+)\s+(\d+)(?:\s+(\w+))?"))
    async def filtr_cmd(event):
        mcap = event.pattern_match.group(1)
        liq = event.pattern_match.group(2)
        chain = event.pattern_match.group(3) or "all"
        conn = await connect()
        try:
            await conn.execute("INSERT INTO user_config(user_id, config_key, config_value) VALUES(0,'min_mcap',$1) ON CONFLICT (user_id,config_key) DO UPDATE SET config_value=EXCLUDED.config_value", mcap)
            await conn.execute("INSERT INTO user_config(user_id, config_key, config_value) VALUES(0,'min_liq',$1) ON CONFLICT (user_id,config_key) DO UPDATE SET config_value=EXCLUDED.config_value", liq)
        finally:
            await conn.close()
        await event.reply(f"Filter updated: mcap>={mcap}, liq>={liq} (chain: {chain})")

    @client.on(events.NewMessage(pattern=r"^/spikesedit\s+(\d+)(?:\s+(\d+))?"))
    async def spikes_cmd(event):
        threshold = event.pattern_match.group(1)
        window = event.pattern_match.group(2) or "300"
        conn = await connect()
        try:
            await conn.execute("INSERT INTO user_config(user_id, config_key, config_value) VALUES(0,'spike_threshold',$1) ON CONFLICT (user_id,config_key) DO UPDATE SET config_value=EXCLUDED.config_value", threshold)
            await conn.execute("INSERT INTO user_config(user_id, config_key, config_value) VALUES(0,'spike_window_sec',$1) ON CONFLICT (user_id,config_key) DO UPDATE SET config_value=EXCLUDED.config_value", window)
        finally:
            await conn.close()
        await event.reply(f"Spike settings: threshold={threshold} msgs, window={window}s")


