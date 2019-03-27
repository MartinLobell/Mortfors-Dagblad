from flask import Flask, render_template, request, flash, redirect, url_for, session
from functools import wraps
import psycopg2

mddb = psycopg2.connect(host = "pgserver.mah.se",
                        user="m11p3220",
                        password = "a4e094h8",
                        database = "m11p3220")

def get_nav_content():
    
    cursor = mddb.cursor()
    get_categories = """SELECT kategorinamn FROM kategori ORDER BY kat_id ASC"""
    cursor.execute(get_categories)
    categories = cursor.fetchall()

    cursor = mddb.cursor()
    get_subcats = """SELECT u.underkategorinamn, u.undkat_id, COUNT(a.art_id)
                     FROM kategori as k
                     JOIN underkategori as u 
                     ON k.kat_id = u.kat_id
                     JOIN artikel as a 
                     ON a.undkat_id = u.undkat_id
                     WHERE k.kat_id=1
                     GROUP BY u.underkategorinamn, u.undkat_id
                     """
    cursor.execute(get_subcats)
    inrikes = cursor.fetchall()

    cursor = mddb.cursor()
    get_subcats = """SELECT u.underkategorinamn, u.undkat_id, COUNT(a.art_id)
                     FROM kategori as k
                     JOIN underkategori as u 
                     ON k.kat_id = u.kat_id
                     JOIN artikel as a 
                     ON a.undkat_id = u.undkat_id
                     WHERE k.kat_id=2
                     GROUP BY u.underkategorinamn, u.undkat_id
                     """
    cursor.execute(get_subcats)
    utrikes = cursor.fetchall()

    cursor = mddb.cursor()
    get_subcats = """SELECT u.underkategorinamn, u.undkat_id, COUNT(a.art_id)
                     FROM kategori as k
                     JOIN underkategori as u 
                     ON k.kat_id = u.kat_id
                     JOIN artikel as a 
                     ON a.undkat_id = u.undkat_id
                     WHERE k.kat_id=3
                     GROUP BY u.underkategorinamn, u.undkat_id
                     """
    cursor.execute(get_subcats)
    sport = cursor.fetchall()

    cursor = mddb.cursor()
    get_subcats = """SELECT u.underkategorinamn, u.undkat_id, COUNT(a.art_id)
                     FROM kategori as k
                     JOIN underkategori as u 
                     ON k.kat_id = u.kat_id
                     JOIN artikel as a 
                     ON a.undkat_id = u.undkat_id
                     WHERE k.kat_id=4
                     GROUP BY u.underkategorinamn, u.undkat_id
                     """
    cursor.execute(get_subcats)
    noje = cursor.fetchall()

    cursor = mddb.cursor()
    get_subcats = """SELECT u.underkategorinamn, u.undkat_id, COUNT(a.art_id)
                     FROM kategori as k
                     JOIN underkategori as u 
                     ON k.kat_id = u.kat_id
                     JOIN artikel as a 
                     ON a.undkat_id = u.undkat_id
                     WHERE k.kat_id=5
                     GROUP BY u.underkategorinamn, u.undkat_id
                     """
    cursor.execute(get_subcats)
    mat = cursor.fetchall()

    data = [inrikes, utrikes, sport, noje, mat]
    return data

def get_quantities():

    cursor = mddb.cursor()
    get_quantity = """SELECT COUNT (a.art_id)
                      FROM artikel as a
                      JOIN underkategori as u
                      ON a.undkat_id = u.undkat_id
                      JOIN kategori as k 
                      ON k.kat_id = u.kat_id
                      WHERE k.kat_id=1
                      GROUP BY k.kat_id
                      """
    cursor.execute(get_quantity)
    inrikes = cursor.fetchall()

    cursor = mddb.cursor()
    get_quantity = """SELECT COUNT (a.art_id)
                      FROM artikel as a
                      JOIN underkategori as u
                      ON a.undkat_id = u.undkat_id
                      JOIN kategori as k 
                      ON k.kat_id = u.kat_id
                      WHERE k.kat_id=2
                      GROUP BY k.kat_id
                      """
    cursor.execute(get_quantity)
    utrikes = cursor.fetchall()

    cursor = mddb.cursor()
    get_quantity = """SELECT COUNT (a.art_id)
                      FROM artikel as a
                      JOIN underkategori as u
                      ON a.undkat_id = u.undkat_id
                      JOIN kategori as k 
                      ON k.kat_id = u.kat_id
                      WHERE k.kat_id=3
                      GROUP BY k.kat_id
                      """
    cursor.execute(get_quantity)
    sport = cursor.fetchall()

    cursor = mddb.cursor()
    get_quantity = """SELECT COUNT (a.art_id)
                      FROM artikel as a
                      JOIN underkategori as u
                      ON a.undkat_id = u.undkat_id
                      JOIN kategori as k 
                      ON k.kat_id = u.kat_id
                      WHERE k.kat_id=4
                      GROUP BY k.kat_id
                      """
    cursor.execute(get_quantity)
    noje = cursor.fetchall()

    cursor = mddb.cursor()
    get_quantity = """SELECT COUNT (a.art_id)
                      FROM artikel as a
                      JOIN underkategori as u
                      ON a.undkat_id = u.undkat_id
                      JOIN kategori as k 
                      ON k.kat_id = u.kat_id
                      WHERE k.kat_id=5
                      GROUP BY k.kat_id
                      """
    cursor.execute(get_quantity)
    mat = cursor.fetchall()

    data = [inrikes, utrikes, sport, noje, mat]
    return data