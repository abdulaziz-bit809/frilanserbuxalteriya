#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""15. Frilanser Buxgalteriya"""
import sqlite3
from datetime import datetime
class Freelance:
    def __init__(self):
        self.conn = sqlite3.connect("freelance.db")
        self.conn.execute("CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY, client TEXT, amount REAL, description TEXT, status TEXT, date TEXT)")
        self.conn.commit()
    def create(self, client, amount, desc):
        self.conn.execute("INSERT INTO invoices VALUES (NULL,?,?,?,'pending',?)", (client, amount, desc, datetime.now().strftime("%Y-%m-%d")))
        self.conn.commit(); print("✅")
    def paid(self, iid):
        self.conn.execute("UPDATE invoices SET status='paid' WHERE id=?", (iid,)); self.conn.commit(); print("✅")
    def totals(self):
        p = self.conn.execute("SELECT SUM(amount) FROM invoices WHERE status='paid'").fetchone()[0] or 0
        pend = self.conn.execute("SELECT SUM(amount) FROM invoices WHERE status='pending'").fetchone()[0] or 0
        return p, pend
def main():
    f = Freelance()
    while True:
        print("\n1.Invoice 2.Tolandi 3.Hisobot 4.Chiqish")
        c = input("> ")
        if c=="1": f.create(input("Mijoz: "), float(input("Summa: ")), input("Tavsif: "))
        elif c=="2": f.paid(int(input("ID: ")))
        elif c=="3":
            p, pend = f.totals(); print(f"Tolangan: {p:,.0f} | Kutilayotgan: {pend:,.0f}")
        elif c=="4": break
if __name__ == "__main__": main()
