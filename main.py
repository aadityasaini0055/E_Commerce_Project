# main.py  —  Project ka entry point
# Yahan se sab kuch chalao

import os
import schedule
import time
from services.etl_service      import run_etl
from reports.report_generator  import generate_report

# Folders banao agar exist nahi karte
os.makedirs("exports", exist_ok=True)
os.makedirs("logs",    exist_ok=True)


def full_pipeline():
    """ETL + Report ek saath"""
    run_etl()
    generate_report()


def show_menu():
    print("""
╔══════════════════════════════════════════╗
║    E-Commerce Analytics Engine          ║
╠══════════════════════════════════════════╣
║  1. ETL chalao  (APIs → Database)         ║
║  2. Report banao  (Database → CSV/JSON)   ║
║  3. Dono karo  (ETL + Report)             ║
║  4. Scheduler  (roz 8 AM auto-run)        ║
║  5. Exit                                  ║
╚══════════════════════════════════════════╝
""")


if __name__ == "__main__":
    show_menu()
    choice = input("  Apna choice likho (1/2/3/4/5): ").strip()

    if choice == "1":
        run_etl()

    elif choice == "2":
        generate_report()

    elif choice == "3":
        full_pipeline()

    elif choice == "4":
        print("\n Scheduler shuru — roz 8:00 AM ko pipeline chalegi")
        print("   Band karne ke liye Ctrl+C dabaao\n")
        full_pipeline()                              # abhi bhi ek baar chalao
        schedule.every().day.at("08:00").do(full_pipeline)
        while True:
            schedule.run_pending()
            time.sleep(60)

    elif choice == "5":
        print(" Bye!")

    else:
        print("Galat choice! 1 se 5 ke beech likho")
