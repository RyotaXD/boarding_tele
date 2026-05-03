# -*- coding: utf-8 -*-

import os
import asyncio
import sys
import time
import random
from datetime import datetime
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
except ImportError:
    os.system('pip install rich')
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
from telethon import TelegramClient

# --- KONFIGURASI API ---
API_ID = # ISI SAMA API_ID AKUN TELEGRAM KALIAN
API_HASH = # 'ISI SAMA API_HASH TELEGRAM KALIAN'

# Settingan pesan
KONTEN = """
ISI CAPTION YANG INGIN DI PAKAI
"""

console = Console()

def get_time():
    return datetime.now().strftime("%H:%M:%S")

async def gas_broadcast(client, group_list, delay_group, loop_count, image_path=None):
    """
    Fungsi utama buat kirim-kirim pesan ke grup
    """
    # Header biar keliatan rapi tiap putaran
    header = Text(f" MENGIRIM BROADCAST - PUTARAN KE-{loop_count} ", style="bold white on blue")
    console.print(Panel(header, border_style="cyan"))
    
    for index, target in enumerate(group_list, 1):
        try:
            # Ambil info grup dulu biar enak liat statusnya
            entitas = await client.get_entity(target)
            nama_group = entitas.title if hasattr(entitas, 'title') else "Private/Unknown"          
            if image_path and os.path.exists(image_path):
                # Kirim pake gambar 
                await client.send_file(entitas, image_path, caption=KONTEN)
                status_txt = "[bold green]SUKSES[/] (Gambar + Teks)"
            else:
                # Kalau gak ada gambar, kirim teks doang
                await client.send_message(entitas, KONTEN, link_preview=True)
                status_txt = "[bold green]SUKSES[/] (Teks Saja)"

            # Print status per grup pake panel
            msg = (
                f"[bold cyan]No      :[/] {index}/{len(group_list)}\n"
                f"[bold cyan]Group   :[/] {nama_group}\n"
                f"[bold cyan]Status  :[/] {status_txt}\n"
                f"[bold cyan]Waktu   :[/] {get_time()}"
            )
            console.print(Panel(msg, border_style="green"))        
        except Exception as e:
            console.print(Panel(f"[bold red]GAGAL[/] ke {target}\n[yellow]Log: {e}[/]", border_style="red"))
        if target != group_list[-1]:
            await asyncio.sleep(delay_group)

async def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Banner utama
    banner = Text("TELEGRAM BROADCASTER", style="bold cyan", justify="center")
    console.print(Panel(banner, padding=(1, 2), border_style="bold blue"))
    print("\n[1] Login via Nomor HP")
    print("[2] Login via Token Bot")
    pilihan = input("\nPilih login (1/2): ")    
    client = TelegramClient('RYEE_SESSION', API_ID, API_HASH)
    if pilihan == '2':
        token = input("Masukkan Token Bot: ")
        await client.start(bot_token=token)
    else:
        await client.start()
    print("-" * 30)
    img_input = input("Path Gambar (kosongkan kalau cuma teks): ").strip()
    image_path = img_input if img_input else None
    inp_groups = input("Input List Group (pisahkan pakai koma): ")
    delay_group = int(input("Jeda antar grup (detik): "))
    delay_loop = int(input("Jeda antar putaran (menit): ")) * 60
    group_list = [g.strip() for g in inp_groups.split(',')]
    loop_count = 1
    console.print(f"\n[bold green]⚡ Script is RUNNING... Tekan CTRL+C buat stop.[/]\n")
    while True:
        try:
            if not client.is_connected():
                await client.connect()
            await gas_broadcast(client, group_list, delay_group, loop_count, image_path)
            waktu_next = datetime.fromtimestamp(time.time() + delay_loop).strftime("%H:%M:%S")
            console.print(Panel(
                f"Putaran [bold yellow]{loop_count}[/] BERES!\nNunggu putaran berikutnya jam: [bold green]{waktu_next}[/]",
                title="[bold magenta]STATUS WAITING[/]",
                subtitle=f"[bold blue]Loop {loop_count} OK[/]",
                border_style="yellow"
            ))
            loop_count += 1
            await asyncio.sleep(delay_loop)
        except Exception as err:
            console.print(Panel(f"ADA ERROR: {err}", border_style="red"))
            await asyncio.sleep(60)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print(f"\n[bold red]Script dihentikan paksa (KeyboardInterrupt).[/]")
        sys.exit()
