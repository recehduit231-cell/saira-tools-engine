# -*- coding: utf-8 -*-
"""
SAIRA 54PERSEN AI TOOLS - BUILDER ENGINE V1
Portal Mega Dashboard 1.000 Alat AI & Utilitas Online Gratis
Single Page Application (SPA) siap pasang di Blogger & Standalone Preview!
"""

import os
import re
import xml.etree.ElementTree as ET

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
XML_OUTPUT_PATH = os.path.join(CURRENT_DIR, "saira-ai-tools-blogger.xml")
PREVIEW_OUTPUT_PATH = os.path.join(CURRENT_DIR, "preview_ai_tools.html")

print("Building SAIRA 54PERSEN AI TOOLS Engine V1...")

# Generate the template content
HTML_TEMPLATE = r"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsversion='3' b:responsive='true' expr:dir='data:blog.languageDirection' lang='id' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
  <meta charset='utf-8'/>
  <meta content='width=device-width, initial-scale=1.0, maximum-scale=5.0' name='viewport'/>
  <title><data:blog.pageTitle/></title>

  <!-- Favicon & Touch Icon -->
  <link href='https://files.catbox.moe/f72xol.jpg' rel='icon' type='image/jpeg'/>
  <link href='https://files.catbox.moe/f72xol.jpg' rel='apple-touch-icon'/>
  <link href='https://files.catbox.moe/f72xol.jpg' rel='image_src'/>

  <!-- ===================== OPEN GRAPH / WHATSAPP / FACEBOOK / TELEGRAM ===================== -->
  <meta content='SAIRA 54PERSEN AI TOOLS' property='og:site_name'/>
  <meta content='website' property='og:type'/>
  <meta content='SAIRA 54PERSEN AI TOOLS - Portal 1.000 Alat AI &amp; Utilitas Online Gratis' property='og:title'/>
  <meta content='Satu Nama, Banyak Solusi! Portal Mega 1.000 Alat AI &amp; Web Utilitas Online: Pengolah Gambar, Desain, Konversi File, AI Writer, Developer Tools, dan Kalkulator instan 100% gratis tanpa login!' property='og:description'/>
  <meta expr:content='data:blog.canonicalUrl' property='og:url'/>

  <!-- Open Graph Image (WhatsApp & Facebook Verified 1024x1024 Square) -->
  <meta content='https://files.catbox.moe/f72xol.jpg' property='og:image'/>
  <meta content='https://files.catbox.moe/f72xol.jpg' property='og:image:secure_url'/>
  <meta content='1024' property='og:image:width'/>
  <meta content='1024' property='og:image:height'/>
  <meta content='image/jpeg' property='og:image:type'/>
  <meta content='SAIRA 54PERSEN AI TOOLS - Portal 1.000 Alat AI &amp; Utilitas Online' property='og:image:alt'/>

  <!-- Twitter Card Meta Tags -->
  <meta content='summary_large_image' name='twitter:card'/>
  <meta content='SAIRA 54PERSEN AI TOOLS - Portal 1.000 Alat AI &amp; Utilitas Online Gratis' name='twitter:title'/>
  <meta content='Satu Nama, Banyak Solusi! Portal Mega 1.000 Alat AI &amp; Web Utilitas Online: Pengolah Gambar, Desain, Konversi File, AI Writer, Developer Tools, dan Kalkulator instan 100% gratis tanpa login!' name='twitter:description'/>
  <meta content='https://files.catbox.moe/f72xol.jpg' name='twitter:image'/>

  <b:include data='blog' name='all-head-content'/>
  <meta content='Portal Mega 1.000 Alat AI &amp; Web Utilitas Online Gratis. Pengolah Gambar, Desain, Konversi File, AI Writer, Developer Tools, dan Kalkulator instan tanpa login!' name='description'/>
  <meta content='saira ai, ai tools, free online tools, image compressor, qr code generator, ai prompt expander, json formatter, convert all' name='keywords'/>
  <meta content='SAIRA 54PERSEN' name='author'/>
  <meta content='#0f172a' name='theme-color'/>

  <!-- Google Fonts: Plus Jakarta Sans, Outfit, JetBrains Mono -->
  <link href='https://fonts.googleapis.com' rel='preconnect'/>
  <link crossorigin='anonymous' href='https://fonts.gstatic.com' rel='preconnect'/>
  <link href='https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&amp;family=Outfit:wght@400;500;600;700;800;900&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap' rel='stylesheet'/>

  <!-- FontAwesome 6 Pro Icons -->
  <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css' rel='stylesheet'/>

  <b:skin><![CDATA[
    /* ================= DESIGN SYSTEM TOKENS ================= */
    :root {
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --accent: #8b5cf6;
      --accent-pink: #ec4899;
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      
      --gradient-brand: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #ec4899 100%);
      --gradient-neon: linear-gradient(135deg, #06b6d4 0%, #3b82f6 50%, #8b5cf6 100%);
      --gradient-card: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(248, 250, 252, 0.9));
      
      --bg-body: #f1f5f9;
      --bg-card: #ffffff;
      --bg-sidebar: #0b1329;
      --bg-topbar: rgba(255, 255, 255, 0.9);
      --border-color: #e2e8f0;
      --border-card: rgba(226, 232, 240, 0.8);
      
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-light: #94a3b8;
      
      --sidebar-w: 260px;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-pill: 9999px;
      
      --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.04);
      --shadow-md: 0 8px 24px rgba(15, 23, 42, 0.06);
      --shadow-lg: 0 16px 36px rgba(15, 23, 42, 0.1);
      --shadow-glow: 0 0 25px rgba(59, 130, 246, 0.25);
    }

    /* Dark Mode Theme */
    body.dark-theme {
      --bg-body: #070d1e;
      --bg-card: #0f172a;
      --bg-sidebar: #050914;
      --bg-topbar: rgba(15, 23, 42, 0.9);
      --border-color: #1e293b;
      --border-card: rgba(255, 255, 255, 0.06);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-light: #64748b;
      --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 16px 36px rgba(0, 0, 0, 0.5);
      --gradient-card: linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.9));
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: var(--bg-body);
      color: var(--text-main);
      line-height: 1.5;
      min-height: 100vh;
      transition: background 0.3s ease, color 0.3s ease;
    }

    a { text-decoration: none; color: inherit; }
    button { font-family: inherit; }

    /* ================= SMOOTH SCROLL & CUSTOM NEON SCROLLBAR ================= */
    html {
      scroll-behavior: smooth;
    }
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-body);
    }
    body.dark-theme ::-webkit-scrollbar-track {
      background: #0b1329;
    }
    ::-webkit-scrollbar-thumb {
      background: linear-gradient(180deg, #3b82f6, #8b5cf6);
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
    }
    ::-webkit-scrollbar-thumb:hover {
      background: linear-gradient(180deg, #2563eb, #ec4899);
      box-shadow: 0 0 14px rgba(236, 72, 153, 0.7);
    }

    /* TOP SCROLL PROGRESS BAR (GLOWING RAINBOW) */
    .scroll-progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 3.5px;
      width: 0%;
      background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899, #06b6d4, #10b981);
      background-size: 300% 100%;
      animation: progressGlow 4s linear infinite;
      z-index: 99999;
      box-shadow: 0 0 14px rgba(59, 130, 246, 0.8), 0 0 28px rgba(236, 72, 153, 0.5);
      transition: width 0.1s ease-out;
      pointer-events: none;
    }
    @keyframes progressGlow {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* FLOATING SCROLL TO TOP BUTTON */
    .scroll-to-top-btn {
      position: fixed;
      bottom: 28px;
      right: 28px;
      width: 46px;
      height: 46px;
      border-radius: 50%;
      background: var(--gradient-brand);
      color: #fff;
      border: none;
      cursor: pointer;
      display: grid;
      place-items: center;
      font-size: 16px;
      box-shadow: 0 8px 24px rgba(59, 130, 246, 0.45);
      z-index: 995;
      opacity: 0;
      visibility: hidden;
      transform: translateY(20px) scale(0.8);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .scroll-to-top-btn.visible {
      opacity: 1;
      visibility: visible;
      transform: translateY(0) scale(1);
    }
    .scroll-to-top-btn:hover {
      transform: translateY(-4px) scale(1.08);
      box-shadow: 0 12px 30px rgba(236, 72, 153, 0.5);
    }

    /* ================= TWO-COLUMN APP LAYOUT ================= */
    .app-layout {
      display: flex;
      min-height: 100vh;
      width: 100%;
      position: relative;
    }

    /* ================= LEFT SIDEBAR (DARK GLOSSY) ================= */
    .app-sidebar {
      width: var(--sidebar-w);
      background: var(--bg-sidebar);
      color: #fff;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 22px 14px;
      position: sticky;
      top: 0;
      height: 100vh;
      overflow-y: auto;
      z-index: 100;
      border-right: 1px solid rgba(255, 255, 255, 0.06);
      transition: margin-left 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s ease;
    }

    .sidebar-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 0 8px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      margin-bottom: 16px;
    }
    .brand-logo-badge {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--gradient-brand);
      color: #fff;
      display: grid;
      place-items: center;
      font-size: 20px;
      box-shadow: 0 4px 16px rgba(59, 130, 246, 0.4);
      animation: pulseBrand 3s infinite alternate;
      flex-shrink: 0;
    }
    @keyframes pulseBrand {
      0% { box-shadow: 0 0 12px rgba(59, 130, 246, 0.3); }
      100% { box-shadow: 0 0 24px rgba(236, 72, 153, 0.5); }
    }
    .brand-title {
      font-family: 'Outfit', sans-serif;
      font-size: 17px;
      font-weight: 900;
      letter-spacing: -0.5px;
      line-height: 1.15;
    }
    .brand-title span {
      background: var(--gradient-brand);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }
    .brand-tagline {
      font-size: 10.5px;
      color: #94a3b8;
      display: block;
      font-weight: 600;
    }

    .sidebar-section-title {
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #64748b;
      padding: 10px 12px 6px;
    }

    .sidebar-nav {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .nav-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
      color: #cbd5e1;
      cursor: pointer;
      transition: all 0.2s;
    }
    .nav-item-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .nav-item-left i {
      width: 18px;
      font-size: 15px;
      text-align: center;
      color: #94a3b8;
      transition: color 0.2s;
    }
    .nav-badge-count {
      font-size: 10px;
      font-weight: 800;
      background: rgba(255, 255, 255, 0.08);
      color: #94a3b8;
      padding: 2px 7px;
      border-radius: var(--radius-pill);
      transition: all 0.2s;
    }
    .nav-item:hover {
      background: rgba(255, 255, 255, 0.06);
      color: #fff;
    }
    .nav-item:hover i {
      color: #38bdf8;
    }
    .nav-item.active {
      background: linear-gradient(135deg, #2563eb, #3b82f6);
      color: #fff;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
    }
    .nav-item.active i {
      color: #fff;
    }
    .nav-item.active .nav-badge-count {
      background: rgba(255, 255, 255, 0.25);
      color: #fff;
    }

    /* Sidebar Footer Status Widget */
    .sidebar-status-widget {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 12px 14px;
      margin-top: 18px;
    }
    .status-indicator-row {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 700;
      color: #10b981;
      margin-bottom: 4px;
    }
    .status-dot-pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 10px #10b981;
      animation: blinkDot 1.5s infinite alternate;
    }
    @keyframes blinkDot {
      0% { opacity: 0.4; transform: scale(0.9); }
      100% { opacity: 1; transform: scale(1.1); }
    }
    .status-info-text {
      font-size: 10px;
      color: #94a3b8;
      line-height: 1.35;
    }

    /* ================= MAIN COLUMN ================= */
    .app-main {
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }

    /* Topbar Header */
    .main-topbar {
      height: 70px;
      background: var(--bg-topbar);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 32px;
      position: sticky;
      top: 0;
      z-index: 990;
      transition: background 0.3s;
    }
    .topbar-left {
      display: flex;
      align-items: center;
      gap: 16px;
      flex: 1;
      max-width: 600px;
    }
    .sidebar-toggle-btn {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: var(--bg-card);
      border: 1.5px solid var(--border-color);
      color: var(--text-main);
      cursor: pointer;
      display: grid;
      place-items: center;
      font-size: 16px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s;
      flex-shrink: 0;
    }
    .sidebar-toggle-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
      transform: scale(1.05);
    }
    .topbar-search-box {
      flex: 1;
      display: flex;
      align-items: center;
      background: var(--bg-card);
      border: 1.5px solid var(--border-color);
      border-radius: var(--radius-pill);
      padding: 0 16px;
      height: 44px;
      gap: 10px;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s;
    }
    .topbar-search-box:focus-within {
      border-color: var(--primary);
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
    }
    .topbar-search-box i {
      color: var(--text-muted);
      font-size: 14px;
    }
    .topbar-search-input {
      flex: 1;
      border: none;
      outline: none;
      background: transparent;
      color: var(--text-main);
      font-size: 13.5px;
      font-weight: 600;
    }
    .topbar-search-input::placeholder {
      color: var(--text-muted);
      font-weight: 500;
    }
    .search-key-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      font-weight: 700;
      color: var(--text-muted);
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      padding: 2px 6px;
      border-radius: 6px;
    }

    .topbar-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .theme-toggle-btn {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: var(--bg-card);
      border: 1.5px solid var(--border-color);
      color: var(--text-main);
      cursor: pointer;
      display: grid;
      place-items: center;
      font-size: 15px;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s;
    }
    .theme-toggle-btn:hover {
      border-color: var(--primary);
      color: var(--primary);
      transform: rotate(20deg);
    }
    .topbar-stat-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
      border: 1px solid rgba(59, 130, 246, 0.25);
      color: var(--primary);
      font-size: 12px;
      font-weight: 800;
      padding: 8px 16px;
      border-radius: var(--radius-pill);
    }

    /* ================= HERO INTRO BANNER ================= */
    .dashboard-hero {
      padding: 36px 36px 24px;
      background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(139, 92, 246, 0.08) 50%, rgba(236, 72, 153, 0.05) 100%);
      border-bottom: 1px solid var(--border-color);
    }
    .hero-badge-tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--gradient-brand);
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      padding: 5px 14px;
      border-radius: var(--radius-pill);
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
      margin-bottom: 14px;
    }
    .hero-title-main {
      font-family: 'Outfit', sans-serif;
      font-size: clamp(26px, 3.2vw, 42px);
      font-weight: 900;
      line-height: 1.15;
      letter-spacing: -0.8px;
      color: var(--text-main);
      margin-bottom: 10px;
    }
    .hero-title-main span {
      background: var(--gradient-brand);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }
    .hero-subtitle-desc {
      font-size: 14px;
      color: var(--text-muted);
      max-width: 680px;
      line-height: 1.5;
      margin-bottom: 20px;
    }

    .hero-features-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
    }
    .feature-chip {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-size: 12px;
      font-weight: 700;
      color: var(--text-main);
      box-shadow: var(--shadow-sm);
    }
    .feature-chip i {
      color: var(--primary);
    }

    /* ================= CATEGORY FILTER PILLS ================= */
    .filter-pills-bar {
      padding: 18px 36px 6px;
      display: flex;
      align-items: center;
      gap: 10px;
      overflow-x: auto;
      white-space: nowrap;
    }
    .cat-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      background: var(--bg-card);
      border: 1.5px solid var(--border-color);
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s;
    }
    .cat-pill:hover {
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-1px);
    }
    .cat-pill.active {
      background: var(--gradient-brand);
      border-color: transparent;
      color: #fff;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35);
    }
    .cat-pill.active i {
      color: #fff;
    }

    /* ================= TOOLS CATALOG GRID ================= */
    .catalog-wrapper {
      padding: 24px 36px 40px;
    }
    .catalog-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
    }
    .catalog-title {
      font-family: 'Outfit', sans-serif;
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: var(--text-main);
    }
    .catalog-count-badge {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
    }

    .tools-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 20px;
    }

    .tool-card {
      background: var(--gradient-card);
      border: 1.5px solid var(--border-card);
      border-radius: var(--radius-lg);
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      box-shadow: var(--shadow-sm);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      cursor: pointer;
      overflow: hidden;
    }
    .tool-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: var(--card-accent, var(--gradient-brand));
      opacity: 0;
      transition: opacity 0.3s;
    }
    .tool-card:hover {
      transform: translateY(-4px);
      border-color: rgba(59, 130, 246, 0.4);
      box-shadow: var(--shadow-md);
    }
    .tool-card:hover::before {
      opacity: 1;
    }

    .tool-card-top {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
    }
    .tool-icon-box {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: var(--icon-bg, linear-gradient(135deg, #3b82f6, #60a5fa));
      color: #fff;
      display: grid;
      place-items: center;
      font-size: 22px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
      flex-shrink: 0;
    }
    .tool-favorite-btn {
      background: transparent;
      border: none;
      color: #cbd5e1;
      font-size: 16px;
      cursor: pointer;
      padding: 4px;
      transition: all 0.2s;
    }
    .tool-favorite-btn:hover {
      color: #f59e0b;
      transform: scale(1.15);
    }
    .tool-favorite-btn.favorited {
      color: #f59e0b;
    }

    .tool-card-info {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .tool-cat-badge {
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--primary);
      background: rgba(59, 130, 246, 0.1);
      padding: 2px 8px;
      border-radius: 6px;
      width: fit-content;
    }
    .tool-title {
      font-family: 'Outfit', sans-serif;
      font-size: 16px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.25;
    }
    .tool-desc {
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .tool-card-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 12px;
      border-top: 1px solid var(--border-color);
    }
    .tool-badge-pill {
      font-size: 11px;
      font-weight: 700;
      color: #10b981;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-run-tool {
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      font-size: 12px;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .tool-card:hover .btn-run-tool {
      background: var(--gradient-brand);
      border-color: transparent;
      color: #fff;
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }

    /* Empty state */
    .empty-catalog-state {
      display: none;
      text-align: center;
      padding: 60px 20px;
      background: var(--bg-card);
      border: 1.5px dashed var(--border-color);
      border-radius: var(--radius-lg);
    }
    .empty-catalog-state i {
      font-size: 48px;
      color: var(--text-muted);
      margin-bottom: 14px;
    }
    .empty-catalog-state h4 {
      font-size: 18px;
      font-weight: 800;
      margin-bottom: 6px;
    }
    .empty-catalog-state p {
      font-size: 13px;
      color: var(--text-muted);
    }

    /* ================= ACTIVE TOOL WORKSPACE (MODAL RUNNER) ================= */
    .tool-modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(8px);
      z-index: 9999;
      opacity: 0;
      transition: opacity 0.3s ease;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .tool-modal-backdrop.active {
      display: flex;
      opacity: 1;
    }
    .tool-modal-container {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 24px;
      width: 100%;
      max-width: 860px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: var(--shadow-lg);
      transform: scale(0.95);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }
    .tool-modal-backdrop.active .tool-modal-container {
      transform: scale(1);
    }
    .tool-modal-header {
      padding: 20px 28px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      background: var(--bg-card);
      z-index: 10;
    }
    .modal-header-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .modal-tool-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--gradient-brand);
      color: #fff;
      display: grid;
      place-items: center;
      font-size: 20px;
    }
    .modal-tool-title {
      font-family: 'Outfit', sans-serif;
      font-size: 18px;
      font-weight: 800;
      color: var(--text-main);
    }
    .modal-tool-cat {
      font-size: 11px;
      font-weight: 700;
      color: var(--primary);
    }
    .modal-close-btn {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      cursor: pointer;
      display: grid;
      place-items: center;
      font-size: 14px;
      transition: all 0.2s;
    }
    .modal-close-btn:hover {
      background: #ef4444;
      border-color: #ef4444;
      color: #fff;
      transform: rotate(90deg);
    }

    .tool-modal-body {
      padding: 28px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Common UI Elements inside Tools */
    .dropzone-box {
      border: 2px dashed #93c5fd;
      background: rgba(59, 130, 246, 0.03);
      border-radius: 16px;
      padding: 32px 20px;
      text-align: center;
      cursor: pointer;
      transition: all 0.25s;
    }
    .dropzone-box:hover, .dropzone-box.dragover {
      border-color: var(--primary);
      background: rgba(59, 130, 246, 0.08);
    }
    .dropzone-icon {
      font-size: 38px;
      color: var(--primary);
      margin-bottom: 10px;
    }
    .dropzone-text strong {
      display: block;
      font-size: 14px;
      color: var(--text-main);
    }
    .dropzone-text span {
      font-size: 12px;
      color: var(--text-muted);
    }

    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .form-group label {
      font-size: 12.5px;
      font-weight: 700;
      color: var(--text-main);
    }
    .form-input, .form-textarea, .form-select {
      background: var(--bg-body);
      border: 1.5px solid var(--border-color);
      color: var(--text-main);
      padding: 10px 14px;
      border-radius: 10px;
      font-family: inherit;
      font-size: 13px;
      outline: none;
      transition: border-color 0.2s;
    }
    .form-input:focus, .form-textarea:focus, .form-select:focus {
      border-color: var(--primary);
    }
    .form-textarea {
      font-family: 'JetBrains Mono', monospace;
      min-height: 120px;
      resize: vertical;
    }

    .btn-action-primary {
      background: var(--gradient-brand);
      color: #fff;
      border: none;
      padding: 12px 22px;
      border-radius: 12px;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(59, 130, 246, 0.35);
      transition: all 0.2s;
    }
    .btn-action-primary:hover {
      filter: brightness(1.1);
      transform: translateY(-1px);
    }
    .btn-action-secondary {
      background: var(--bg-body);
      color: var(--text-main);
      border: 1.5px solid var(--border-color);
      padding: 11px 18px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-action-secondary:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .output-card-box {
      background: var(--bg-body);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .output-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      font-weight: 800;
      color: var(--text-muted);
    }
    .output-content-pre {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px;
      line-height: 1.5;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px;
      white-space: pre-wrap;
      word-break: break-all;
      max-height: 240px;
      overflow-y: auto;
      color: var(--text-main);
    }

    /* ================= FOOTER ================= */
    .dashboard-footer {
      background: var(--bg-sidebar);
      color: #fff;
      padding: 24px 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      margin-top: auto;
    }
    .footer-left-brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .footer-brand-title {
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 15px;
    }
    .footer-brand-sub {
      font-size: 11px;
      color: #64748b;
    }
    .footer-copyright {
      font-size: 11px;
      color: #64748b;
    }

    /* Desktop Collapsed Sidebar State */
    @media (min-width: 901px) {
      body.sidebar-collapsed .app-sidebar {
        margin-left: calc(-1 * var(--sidebar-w));
        opacity: 0;
        pointer-events: none;
      }
      body.sidebar-collapsed .app-main {
        width: 100%;
      }
      body.sidebar-collapsed .topbar-desktop-brand {
        display: flex;
      }
    }

    .topbar-desktop-brand {
      display: none;
      align-items: center;
      text-decoration: none;
      color: var(--text-main);
      margin-left: 4px;
    }

    /* Blogger Required Widget */
    .blogger-section { display: none !important; }

    /* ================= RESPONSIVE MOBILE QUERIES ================= */
    @media (max-width: 900px) {
      html, body {
        overflow-x: hidden;
      }
      .app-sidebar {
        position: fixed;
        left: 0;
        top: 0;
        bottom: 0;
        height: 100vh;
        z-index: 1000;
        transform: translateX(-100%);
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.6);
      }
      body.sidebar-mobile-open .app-sidebar {
        transform: translateX(0);
      }
      .topbar-desktop-brand {
        display: flex;
      }
      .main-topbar {
        padding: 0 16px;
        height: 62px;
      }
      .topbar-stat-pill {
        display: none;
      }
      .search-key-badge {
        display: none;
      }
      .dashboard-hero {
        padding: 24px 16px 20px;
      }
      .filter-pills-bar {
        padding: 14px 16px 4px;
      }
      .catalog-wrapper {
        padding: 18px 16px 36px;
      }
      .tools-grid {
        grid-template-columns: 1fr;
        gap: 14px;
      }
      .tool-modal-backdrop {
        padding: 10px;
      }
      .tool-modal-body {
        padding: 18px 16px;
      }
      .dashboard-footer {
        padding: 20px 16px;
        flex-direction: column;
        align-items: flex-start;
      }
    }
  ]]></b:skin>
</head>
<body>

  <!-- HIDDEN FALLBACK IMAGE FOR WHATSAPP/FACEBOOK CRAWLER -->
  <div style='display:none; visibility:hidden; position:absolute; left:-9999px;'><img alt='SAIRA 54PERSEN AI TOOLS' src='https://files.catbox.moe/f72xol.jpg'/></div>

  <!-- TOP SCROLL PROGRESS INDICATOR -->
  <div class='scroll-progress-bar' id='scrollProgressBar'></div>

  <!-- FLOATING SCROLL TO TOP BUTTON -->
  <button class='scroll-to-top-btn' id='scrollToTopBtn' onclick='scrollToTop()' title='Kembali ke Atas' type='button'>
    <i class='fas fa-arrow-up'></i>
  </button>

  <!-- MOBILE SIDEBAR BACKDROP -->
  <div class='tool-modal-backdrop' id='sidebarBackdrop' onclick='toggleSidebar()'></div>

  <div class='app-layout'>
    <!-- LEFT SIDEBAR -->
    <aside class='app-sidebar'>
      <div>
        <div class='sidebar-brand'>
          <div class='brand-logo-badge'><i class='fas fa-brain'></i></div>
          <div>
            <div class='brand-title'>SAIRA <span>54PERSEN</span></div>
            <span class='brand-tagline'>Portal 1.000 Alat AI &amp; Utilitas</span>
          </div>
        </div>

        <div class='sidebar-section-title'>Navigasi Cepat</div>
        <nav class='sidebar-nav'>
          <div class='nav-item active' onclick='filterCategory("all", this)'>
            <div class='nav-item-left'><i class='fas fa-bolt'></i> <span>Semua Tools</span></div>
            <span class='nav-badge-count' id='countAll'>26</span>
          </div>
          <div class='nav-item' onclick='filterFavorites(this)'>
            <div class='nav-item-left'><i class='fas fa-star' style='color:#f59e0b;'></i> <span>Favorit Saya</span></div>
            <span class='nav-badge-count' id='countFav'>0</span>
          </div>
        </nav>

        <div class='sidebar-section-title' style='margin-top:16px;'>Kategori Alat</div>
        <nav class='sidebar-nav'>
          <div class='nav-item' onclick='filterCategory("image", this)'>
            <div class='nav-item-left'><i class='fas fa-image' style='color:#38bdf8;'></i> <span>AI Image</span></div>
            <span class='nav-badge-count'>5</span>
          </div>
          <div class='nav-item' onclick='filterCategory("design", this)'>
            <div class='nav-item-left'><i class='fas fa-palette' style='color:#ec4899;'></i> <span>AI Design &amp; Art</span></div>
            <span class='nav-badge-count'>4</span>
          </div>
          <div class='nav-item' onclick='filterCategory("convert", this)'>
            <div class='nav-item-left'><i class='fas fa-arrows-rotate' style='color:#10b981;'></i> <span>Convert All</span></div>
            <span class='nav-badge-count'>4</span>
          </div>
          <div class='nav-item' onclick='filterCategory("writer", this)'>
            <div class='nav-item-left'><i class='fas fa-pen-nib' style='color:#8b5cf6;'></i> <span>AI Writer &amp; Copy</span></div>
            <span class='nav-badge-count'>5</span>
          </div>
          <div class='nav-item' onclick='filterCategory("dev", this)'>
            <div class='nav-item-left'><i class='fas fa-code' style='color:#f59e0b;'></i> <span>Developer Tools</span></div>
            <span class='nav-badge-count'>5</span>
          </div>
          <div class='nav-item' onclick='filterCategory("utility", this)'>
            <div class='nav-item-left'><i class='fas fa-calculator' style='color:#06b6d4;'></i> <span>Utilitas &amp; Hitung</span></div>
            <span class='nav-badge-count'>3</span>
          </div>
        </nav>
      </div>

      <div class='sidebar-status-widget'>
        <div class='status-indicator-row'>
          <span class='status-dot-pulse'></span>
          <span>SAIRA Engine V1 Active</span>
        </div>
        <div class='status-info-text'>100% Client-Side Processing. Cepat, aman tanpa batas &amp; bebas kuota!</div>
      </div>
    </aside>

    <!-- MAIN COLUMN -->
    <div class='app-main'>
      <!-- TOPBAR -->
      <header class='main-topbar'>
        <div class='topbar-left'>
          <button class='sidebar-toggle-btn' onclick='toggleSidebar()' title='Menu' type='button'>
            <i class='fas fa-bars'></i>
          </button>
          <a class='topbar-desktop-brand' href='#'>
            <div class='brand-logo-badge' style='width:32px; height:32px; font-size:14px;'><i class='fas fa-brain'></i></div>
            <span style='font-family:Outfit; font-weight:800; font-size:15px; margin-left:8px;'>SAIRA <span style='color:var(--primary);'>54PERSEN</span></span>
          </a>
          <div class='topbar-search-box'>
            <i class='fas fa-search'></i>
            <input autocomplete='off' class='topbar-search-input' id='globalSearchInput' oninput='handleLiveSearch()' placeholder='Cari alat (misal: kompres, qr, prompt, json, case)...' type='text'/>
            <span class='search-key-badge'>Ctrl + K</span>
          </div>
        </div>

        <div class='topbar-actions'>
          <div class='topbar-stat-pill'>
            <i class='fas fa-bolt'></i> <span>26 Alat Siap Pakai</span>
          </div>
          <button class='theme-toggle-btn' onclick='toggleTheme()' title='Mode Gelap/Terang' type='button'>
            <i class='fas fa-moon' id='themeIcon'></i>
          </button>
        </div>
      </header>

      <!-- HERO INTRO BANNER -->
      <section class='dashboard-hero'>
        <div class='hero-badge-tag'><i class='fas fa-wand-magic-sparkles'></i> SAIRA 54PERSEN AI TOOLS ENGINE</div>
        <h1 class='hero-title-main'>Satu Nama, <span>Banyak Solusi!</span></h1>
        <p class='hero-subtitle-desc'>Koleksi alat bantu AI, pengolah gambar, generator desain, konverter format, dan utilitas developer serbaguna. Langsung diproses di browsermu — 100% gratis, aman &amp; instan!</p>
        
        <div class='hero-features-chips'>
          <div class='feature-chip'><i class='fas fa-shield-halved'></i> 100% Privasi Aman</div>
          <div class='feature-chip'><i class='fas fa-bolt'></i> Kecepatan Browser Native</div>
          <div class='feature-chip'><i class='fas fa-circle-check'></i> Tanpa Login / Bebas Biaya</div>
          <div class='feature-chip'><i class='fas fa-mobile-screen'></i> Responsif HP &amp; PC</div>
        </div>
      </section>

      <!-- CATEGORY FILTER PILLS -->
      <div class='filter-pills-bar' id='categoryPillsBar'>
        <button class='cat-pill active' onclick='filterCategory("all", this)' type='button'><i class='fas fa-border-all'></i> Semua Alat</button>
        <button class='cat-pill' onclick='filterCategory("image", this)' type='button'><i class='fas fa-image'></i> AI Image</button>
        <button class='cat-pill' onclick='filterCategory("design", this)' type='button'><i class='fas fa-palette'></i> AI Design</button>
        <button class='cat-pill' onclick='filterCategory("convert", this)' type='button'><i class='fas fa-arrows-rotate'></i> Convert All</button>
        <button class='cat-pill' onclick='filterCategory("writer", this)' type='button'><i class='fas fa-pen-nib'></i> AI Writer</button>
        <button class='cat-pill' onclick='filterCategory("dev", this)' type='button'><i class='fas fa-code'></i> Developer Tools</button>
        <button class='cat-pill' onclick='filterCategory("utility", this)' type='button'><i class='fas fa-calculator'></i> Utilitas</button>
      </div>

      <!-- TOOLS CATALOG GRID -->
      <section class='catalog-wrapper'>
        <div class='catalog-header'>
          <h2 class='catalog-title' id='currentCatalogTitle'>Katalog Alat Aktif</h2>
          <span class='catalog-count-badge' id='visibleToolsCount'>Menampilkan 26 alat</span>
        </div>

        <div class='tools-grid' id='toolsGridContainer'>
          <!-- Tool cards will be dynamically rendered via JS -->
        </div>

        <!-- Empty search state -->
        <div class='empty-catalog-state' id='emptyCatalogState'>
          <i class='fas fa-magnifying-glass'></i>
          <h4>Alat Tidak Ditemukan</h4>
          <p>Coba gunakan kata kunci lain seperti "kompres", "qr", "format", atau "prompt".</p>
        </div>
      </section>

      <!-- FOOTER -->
      <footer class='dashboard-footer'>
        <div class='footer-left-brand'>
          <div class='brand-logo-badge' style='width:34px; height:34px; font-size:15px;'><i class='fas fa-brain'></i></div>
          <div>
            <div class='footer-brand-title'>SAIRA 54PERSEN AI TOOLS</div>
            <div class='footer-brand-sub'>Portal 1.000 Alat AI &amp; Web Utilitas Terlengkap</div>
          </div>
        </div>
        <div class='footer-copyright'>
          &#169; 2026 SAIRA 54PERSEN. Dikembangkan untuk kemudahan produktivitas digital.
        </div>
      </footer>
    </div>
  </div>

  <!-- INTERACTIVE TOOL RUNNER MODAL WORKSPACE -->
  <div class='tool-modal-backdrop' id='toolModalBackdrop'>
    <div class='tool-modal-container'>
      <div class='tool-modal-header'>
        <div class='modal-header-left'>
          <div class='modal-tool-icon' id='modalToolIcon'><i class='fas fa-tools'></i></div>
          <div>
            <div class='modal-tool-title' id='modalToolTitle'>Nama Alat</div>
            <span class='modal-tool-cat' id='modalToolCat'>Kategori</span>
          </div>
        </div>
        <button class='modal-close-btn' onclick='closeToolModal()' title='Tutup' type='button'>
          <i class='fas fa-times'></i>
        </button>
      </div>

      <div class='tool-modal-body' id='toolModalBody'>
        <!-- Dynamic Tool Interactive Controls will be injected here -->
      </div>
    </div>
  </div>

  <!-- BLOGGER SYSTEM REQUIRED WIDGET (HIDDEN) -->
  <b:section class='blogger-section' id='main' maxwidgets='1' showaddelement='no'>
    <b:widget id='Blog1' locked='true' title='Postingan Blog' type='Blog' visible='false'/>
  </b:section>

  <!-- CORE SCRIPT ENGINE -->
  <script type='text/javascript'>
  //<![CDATA[
  /* ================= SAIRA 54PERSEN AI TOOLS - CLIENT ENGINE V1 ================= */

  // 1. TOOL REGISTRY DATA (26 Functional Tools)
  var TOOLS_REGISTRY = [
    // --- AI IMAGE TOOLS ---
    {
      id: 'img-compress',
      name: 'Image Compressor Pro',
      cat: 'image',
      catName: 'AI Image',
      icon: 'fas fa-file-zipper',
      iconBg: 'linear-gradient(135deg, #0284c7, #38bdf8)',
      desc: 'Kompres ukuran file gambar JPG, PNG, dan WebP secara instan dengan slider kualitas cerdas.',
      badge: 'Browser Native',
      tags: ['kompres', 'foto', 'compress', 'gambar', 'jpg', 'png', 'webp', 'reduce', 'size']
    },
    {
      id: 'img-resize',
      name: 'Image Resizer & Scaler',
      cat: 'image',
      catName: 'AI Image',
      icon: 'fas fa-up-right-and-down-left-from-center',
      iconBg: 'linear-gradient(135deg, #0ea5e9, #6366f1)',
      desc: 'Ubah dimensi lebar dan tinggi resolusi foto secara proporsional dengan kunci rasio aspek.',
      badge: 'Pixel Perfect',
      tags: ['resize', 'skala', 'ukuran', 'resolusi', 'crop', 'dimensi', 'foto']
    },
    {
      id: 'img-convert',
      name: 'Image Format Converter',
      cat: 'image',
      catName: 'AI Image',
      icon: 'fas fa-repeat',
      iconBg: 'linear-gradient(135deg, #2563eb, #38bdf8)',
      desc: 'Konversi format gambar instan antara JPG, PNG, dan WebP tanpa kehilangan ketajaman.',
      badge: 'Instant Convert',
      tags: ['convert', 'format', 'jpg to png', 'png to webp', 'ubah', 'ekstensi']
    },
    {
      id: 'img-palette',
      name: 'Color Palette Extractor',
      cat: 'image',
      catName: 'AI Image',
      icon: 'fas fa-eye-dropper',
      iconBg: 'linear-gradient(135deg, #06b6d4, #10b981)',
      desc: 'Ekstrak palet 6 warna dominan dari gambar apa pun lengkap dengan kode HEX & RGB 1-klik salin.',
      badge: 'Design Palette',
      tags: ['palette', 'warna', 'color', 'hex', 'rgb', 'picker', 'extract']
    },
    {
      id: 'img-base64',
      name: 'Image to Base64 Encoder',
      cat: 'image',
      catName: 'AI Image',
      icon: 'fas fa-code',
      iconBg: 'linear-gradient(135deg, #3b82f6, #8b5cf6)',
      desc: 'Konversi file gambar menjadi string Base64 Data URI siap pakai untuk tag HTML img dan CSS.',
      badge: 'Web Ready',
      tags: ['base64', 'data uri', 'encode', 'gambar', 'code', 'inline']
    },

    // --- AI DESIGN TOOLS ---
    {
      id: 'qr-studio',
      name: 'QR Code Studio Pro',
      cat: 'design',
      catName: 'AI Design & Art',
      icon: 'fas fa-qrcode',
      iconBg: 'linear-gradient(135deg, #ec4899, #f43f5e)',
      desc: 'Buat kode QR kustom untuk Tautan, Teks, WiFi, dan WhatsApp dengan warna kustom dan unduh PNG.',
      badge: 'Vector Sharp',
      tags: ['qr', 'barcode', 'link', 'generator', 'wifi', 'whatsapp', 'unduh']
    },
    {
      id: 'css-gradient',
      name: 'CSS Gradient Studio',
      cat: 'design',
      catName: 'AI Design & Art',
      icon: 'fas fa-swatchbook',
      iconBg: 'linear-gradient(135deg, #f43f5e, #fb923c)',
      desc: 'Rancang perpaduan warna gradient linear dan radial modern dengan live preview dan salin CSS.',
      badge: 'CSS3 Code',
      tags: ['gradient', 'css', 'warna', 'linear', 'radial', 'background', 'desain']
    },
    {
      id: 'css-glass',
      name: 'Glassmorphism Generator',
      cat: 'design',
      catName: 'AI Design & Art',
      icon: 'fas fa-wand-magic-sparkles',
      iconBg: 'linear-gradient(135deg, #8b5cf6, #ec4899)',
      desc: 'Atur efek blur kaca transparan kekinian, tingkat opacity, dan border glow dengan salin kode CSS.',
      badge: 'Modern UI',
      tags: ['glassmorphism', 'blur', 'kaca', 'transparan', 'css', 'frosted']
    },
    {
      id: 'css-shadow',
      name: 'Box Shadow Generator',
      cat: 'design',
      catName: 'AI Design & Art',
      icon: 'fas fa-clone',
      iconBg: 'linear-gradient(135deg, #a855f7, #6366f1)',
      desc: 'Buat bayangan bayangan halus bertingkat (soft layered shadow) dengan preview langsung.',
      badge: 'CSS Shadow',
      tags: ['shadow', 'bayangan', 'box shadow', 'css', 'elevation']
    },

    // --- CONVERT ALL TOOLS ---
    {
      id: 'b64-text',
      name: 'Base64 Text Encoder/Decoder',
      cat: 'convert',
      catName: 'Convert All',
      icon: 'fas fa-right-left',
      iconBg: 'linear-gradient(135deg, #10b981, #059669)',
      desc: 'Enkripsi dan dekripsi teks biasa menjadi Base64 string dua arah secara instan dan aman.',
      badge: 'Dual Mode',
      tags: ['base64', 'encode', 'decode', 'teks', 'enkripsi', 'dekripsi']
    },
    {
      id: 'json-csv',
      name: 'JSON to CSV Converter',
      cat: 'convert',
      catName: 'Convert All',
      icon: 'fas fa-table',
      iconBg: 'linear-gradient(135deg, #059669, #10b981)',
      desc: 'Ubah format data JSON menjadi berkas tabel CSV yang rapi dan siap dibuka di Microsoft Excel.',
      badge: 'Data Tools',
      tags: ['json', 'csv', 'excel', 'convert', 'tabel', 'data']
    },
    {
      id: 'text-binary',
      name: 'Text to Binary & Hex',
      cat: 'convert',
      catName: 'Convert All',
      icon: 'fas fa-microchip',
      iconBg: 'linear-gradient(135deg, #0d9488, #14b8a6)',
      desc: 'Konversi teks menjadi kode biner 0 dan 1 atau Heksadesimal mesin, serta sebaliknya.',
      badge: 'Binary Tools',
      tags: ['biner', 'binary', 'hex', '0101', 'mesin', 'konversi']
    },
    {
      id: 'url-slug',
      name: 'URL Slug Generator',
      cat: 'convert',
      catName: 'Convert All',
      icon: 'fas fa-link',
      iconBg: 'linear-gradient(135deg, #10b981, #3b82f6)',
      desc: 'Ubah judul artikel panjang menjadi link URL yang ramah SEO (kebab-case) bebas karakter aneh.',
      badge: 'SEO Friendly',
      tags: ['slug', 'url', 'seo', 'link', 'kebab-case', 'artikel']
    },

    // --- AI WRITER & TEXT UTILITY ---
    {
      id: 'ai-prompt',
      name: 'AI Prompt Expander',
      cat: 'writer',
      catName: 'AI Writer & Copy',
      icon: 'fas fa-robot',
      iconBg: 'linear-gradient(135deg, #8b5cf6, #3b82f6)',
      desc: 'Kembangkan ide prompt singkat menjadi prompt Midjourney & ChatGPT level master dengan 6 gaya seni.',
      badge: 'Prompt Master',
      tags: ['prompt', 'midjourney', 'chatgpt', 'ai', 'generate', 'expander', 'seni']
    },
    {
      id: 'ai-caption',
      name: 'AI Caption & Hashtag Creator',
      cat: 'writer',
      catName: 'AI Writer & Copy',
      icon: 'fas fa-hashtag',
      iconBg: 'linear-gradient(135deg, #ec4899, #8b5cf6)',
      desc: 'Hasilkan caption media sosial viral untuk Instagram & TikTok lengkap dengan kumpulan hashtag trending.',
      badge: 'Social Viral',
      tags: ['caption', 'hashtag', 'instagram', 'tiktok', 'sosmed', 'viral', 'konten']
    },
    {
      id: 'word-counter',
      name: 'Word & Character Counter Pro',
      cat: 'writer',
      catName: 'AI Writer & Copy',
      icon: 'fas fa-chart-simple',
      iconBg: 'linear-gradient(135deg, #6366f1, #8b5cf6)',
      desc: 'Hitung jumlah kata, karakter dengan/tanpa spasi, jumlah kalimat, paragraf, serta estimasi waktu baca.',
      badge: 'Analytics',
      tags: ['word count', 'karakter', 'hitung kata', 'paragraf', 'kecepatan baca']
    },
    {
      id: 'case-converter',
      name: 'Text Case Converter',
      cat: 'writer',
      catName: 'AI Writer & Copy',
      icon: 'fas fa-font',
      iconBg: 'linear-gradient(135deg, #a855f7, #ec4899)',
      desc: 'Ubah gaya huruf teks menjadi UPPERCASE, lowercase, Title Case, camelCase, snake_case, dan kebab-case.',
      badge: 'Format Text',
      tags: ['case', 'huruf besar', 'huruf kecil', 'capital', 'camelcase', 'snake_case']
    },
    {
      id: 'lorem-ipsum',
      name: 'Lorem Ipsum Generator',
      cat: 'writer',
      catName: 'AI Writer & Copy',
      icon: 'fas fa-paragraph',
      iconBg: 'linear-gradient(135deg, #7c3aed, #a855f7)',
      desc: 'Hasilkan teks dummy placeholder standar industri desain dalam hitungan paragraf, kalimat, atau kata.',
      badge: 'Dummy Text',
      tags: ['lorem', 'ipsum', 'dummy', 'placeholder', 'mockup', 'teks']
    },

    // --- DEVELOPER TOOLS ---
    {
      id: 'json-format',
      name: 'JSON Formatter & Validator',
      cat: 'dev',
      catName: 'Developer Tools',
      icon: 'fas fa-file-code',
      iconBg: 'linear-gradient(135deg, #f59e0b, #d97706)',
      desc: 'Rapikan indentasi kode JSON yang berantakan, perkecil (minify), dan temukan posisi error sintaks.',
      badge: 'Clean Code',
      tags: ['json', 'format', 'beautify', 'validate', 'minify', 'developer']
    },
    {
      id: 'code-minify',
      name: 'HTML & CSS Minifier',
      cat: 'dev',
      catName: 'Developer Tools',
      icon: 'fas fa-compress',
      iconBg: 'linear-gradient(135deg, #d97706, #b45309)',
      desc: 'Hapus spasi dan baris kosong dari file HTML atau CSS untuk meningkatkan kecepatan loading website.',
      badge: 'Speed Boost',
      tags: ['minify', 'kompres kode', 'html', 'css', 'optimasi', 'web']
    },
    {
      id: 'uuid-gen',
      name: 'UUID / GUID v4 Generator',
      cat: 'dev',
      catName: 'Developer Tools',
      icon: 'fas fa-fingerprint',
      iconBg: 'linear-gradient(135deg, #ea580c, #f59e0b)',
      desc: 'Hasilkan identifier unik acak standar UUID versi 4 (v4) satu per satu atau sekaligus banyak.',
      badge: 'Crypto Safe',
      tags: ['uuid', 'guid', 'unique id', 'token', 'acak', 'random']
    },
    {
      id: 'pass-gen',
      name: 'Password Generator Pro',
      cat: 'dev',
      catName: 'Developer Tools',
      icon: 'fas fa-key',
      iconBg: 'linear-gradient(135deg, #b45309, #d97706)',
      desc: 'Buat kata sandi acak super kuat yang tahan serangan brute-force dengan pengukur kekuatan sandi.',
      badge: 'Security',
      tags: ['password', 'sandi', 'keamanan', 'generator', 'strong', 'secure']
    },
    {
      id: 'hash-gen',
      name: 'Crypto Hash Generator',
      cat: 'dev',
      catName: 'Developer Tools',
      icon: 'fas fa-shield-halved',
      iconBg: 'linear-gradient(135deg, #f59e0b, #ef4444)',
      desc: 'Hitung nilai hash kriptografi SHA-256, SHA-1, dan SHA-512 dari teks apa pun menggunakan Web Crypto API.',
      badge: 'Web Crypto',
      tags: ['hash', 'sha256', 'sha1', 'sha512', 'kripto', 'keamanan']
    },

    // --- CALCULATORS & UTILITIES ---
    {
      id: 'calc-discount',
      name: 'Kalkulator Diskon & Belanja',
      cat: 'utility',
      catName: 'Utilitas & Hitung',
      icon: 'fas fa-tags',
      iconBg: 'linear-gradient(135deg, #06b6d4, #0284c7)',
      desc: 'Hitung harga akhir setelah diskon, potongan uang yang didapat, dan total hemat belanjaan seketika.',
      badge: 'Shopping',
      tags: ['diskon', 'kalkulator', 'belanja', 'promo', 'hemat', 'persen']
    },
    {
      id: 'calc-age',
      name: 'Kalkulator Usia & Ulang Tahun',
      cat: 'utility',
      catName: 'Utilitas & Hitung',
      icon: 'fas fa-cake-candles',
      iconBg: 'linear-gradient(135deg, #0284c7, #2563eb)',
      desc: 'Hitung usia akurat hingga hitungan tahun, bulan, hari, serta hitung mundur ke ulang tahun berikutnya.',
      badge: 'Exact Age',
      tags: ['usia', 'umur', 'ulang tahun', 'tanggal', 'kalkulator']
    },
    {
      id: 'calc-aspect',
      name: 'Aspect Ratio Calculator',
      cat: 'utility',
      catName: 'Utilitas & Hitung',
      icon: 'fas fa-display',
      iconBg: 'linear-gradient(135deg, #0891b2, #06b6d4)',
      desc: 'Hitung rasio aspek layar dan resolusi target (16:9, 4:3, 1:1, 9:16) untuk video dan grafis.',
      badge: 'Screen Tools',
      tags: ['aspect ratio', '16:9', 'layar', 'resolusi', 'lebar', 'tinggi']
    }
  ];

  // 2. FAVORITES MANAGEMENT
  var favoritesSet = new Set();
  try {
    var rawFav = localStorage.getItem('saira_ai_favorites');
    if (rawFav) favoritesSet = new Set(JSON.parse(rawFav));
  } catch(e) {}

  function saveFavorites() {
    try {
      localStorage.setItem('saira_ai_favorites', JSON.stringify(Array.from(favoritesSet)));
      updateFavBadgeCount();
    } catch(e) {}
  }

  function toggleFavorite(toolId, e) {
    if (e) e.stopPropagation();
    if (favoritesSet.has(toolId)) {
      favoritesSet.delete(toolId);
    } else {
      favoritesSet.add(toolId);
    }
    saveFavorites();
    renderToolsGrid(currentFilteredTools);
  }

  function updateFavBadgeCount() {
    var badge = document.getElementById('countFav');
    if (badge) badge.innerText = favoritesSet.size;
  }

  // 3. CATALOG RENDERING & FILTERING
  var activeCategory = 'all';
  var currentFilteredTools = TOOLS_REGISTRY.slice();

  function renderToolsGrid(toolsList) {
    var container = document.getElementById('toolsGridContainer');
    var emptyState = document.getElementById('emptyCatalogState');
    var countBadge = document.getElementById('visibleToolsCount');
    if (!container) return;

    if (toolsList.length === 0) {
      container.innerHTML = '';
      if (emptyState) emptyState.style.display = 'block';
      if (countBadge) countBadge.innerText = '0 alat ditemukan';
      return;
    }

    if (emptyState) emptyState.style.display = 'none';
    if (countBadge) countBadge.innerText = 'Menampilkan ' + toolsList.length + ' alat';

    var html = '';
    for (var i = 0; i < toolsList.length; i++) {
      var t = toolsList[i];
      var isFav = favoritesSet.has(t.id);
      html += `
        <div class="tool-card" onclick="openToolModal('${t.id}')">
          <div>
            <div class="tool-card-top">
              <div class="tool-icon-box" style="background:${t.iconBg};">
                <i class="${t.icon}"></i>
              </div>
              <button class="tool-favorite-btn ${isFav ? 'favorited' : ''}" onclick="toggleFavorite('${t.id}', event)" title="Simpan ke Favorit" type="button">
                <i class="${isFav ? 'fas fa-star' : 'far fa-star'}"></i>
              </button>
            </div>
            <div class="tool-card-info" style="margin-top: 14px;">
              <span class="tool-cat-badge">${t.catName}</span>
              <h3 class="tool-title">${t.name}</h3>
              <p class="tool-desc">${t.desc}</p>
            </div>
          </div>
          <div class="tool-card-bottom">
            <span class="tool-badge-pill"><i class="fas fa-check-circle"></i> ${t.badge}</span>
            <span class="btn-run-tool">Gunakan <i class="fas fa-arrow-right"></i></span>
          </div>
        </div>
      `;
    }
    container.innerHTML = html;
  }

  function filterCategory(cat, el) {
    activeCategory = cat;
    // update sidebar pills
    var navItems = document.querySelectorAll('.sidebar-nav .nav-item');
    navItems.forEach(function(item) { item.classList.remove('active'); });
    if (el) el.classList.add('active');

    // update horizontal pills
    var pills = document.querySelectorAll('.cat-pill');
    pills.forEach(function(p) {
      if (p.getAttribute('onclick') && p.getAttribute('onclick').indexOf("'" + cat + "'") !== -1) {
        p.classList.add('active');
      } else {
        p.classList.remove('active');
      }
    });

    var titleEl = document.getElementById('currentCatalogTitle');
    if (cat === 'all') {
      currentFilteredTools = TOOLS_REGISTRY.slice();
      if (titleEl) titleEl.innerText = 'Katalog Semua Alat';
    } else {
      currentFilteredTools = TOOLS_REGISTRY.filter(function(t) { return t.cat === cat; });
      if (titleEl) titleEl.innerText = 'Kategori: ' + (currentFilteredTools[0] ? currentFilteredTools[0].catName : cat);
    }
    renderToolsGrid(currentFilteredTools);
  }

  function filterFavorites(el) {
    var navItems = document.querySelectorAll('.sidebar-nav .nav-item');
    navItems.forEach(function(item) { item.classList.remove('active'); });
    if (el) el.classList.add('active');

    var pills = document.querySelectorAll('.cat-pill');
    pills.forEach(function(p) { p.classList.remove('active'); });

    currentFilteredTools = TOOLS_REGISTRY.filter(function(t) { return favoritesSet.has(t.id); });
    var titleEl = document.getElementById('currentCatalogTitle');
    if (titleEl) titleEl.innerText = 'Alat Favorit Saya (' + currentFilteredTools.length + ')';
    renderToolsGrid(currentFilteredTools);
  }

  function handleLiveSearch() {
    var input = document.getElementById('globalSearchInput');
    if (!input) return;
    var query = input.value.trim().toLowerCase();

    if (!query) {
      filterCategory(activeCategory);
      return;
    }

    currentFilteredTools = TOOLS_REGISTRY.filter(function(t) {
      if (t.name.toLowerCase().indexOf(query) !== -1) return true;
      if (t.desc.toLowerCase().indexOf(query) !== -1) return true;
      if (t.catName.toLowerCase().indexOf(query) !== -1) return true;
      for (var i = 0; i < t.tags.length; i++) {
        if (t.tags[i].indexOf(query) !== -1) return true;
      }
      return false;
    });

    var titleEl = document.getElementById('currentCatalogTitle');
    if (titleEl) titleEl.innerText = 'Hasil Pencarian: "' + query + '"';
    renderToolsGrid(currentFilteredTools);
  }

  // 4. INTERACTIVE TOOL WORKSPACE RUNNER
  function openToolModal(toolId) {
    var tool = TOOLS_REGISTRY.find(function(t) { return t.id === toolId; });
    if (!tool) return;

    var backdrop = document.getElementById('toolModalBackdrop');
    var iconEl = document.getElementById('modalToolIcon');
    var titleEl = document.getElementById('modalToolTitle');
    var catEl = document.getElementById('modalToolCat');
    var bodyEl = document.getElementById('toolModalBody');

    if (iconEl) iconEl.innerHTML = '<i class="' + tool.icon + '"></i>';
    if (titleEl) titleEl.innerText = tool.name;
    if (catEl) catEl.innerText = tool.catName + ' · ' + tool.badge;

    // Render specific tool UI
    if (bodyEl) {
      bodyEl.innerHTML = buildToolUI(tool);
      initToolLogic(tool.id);
    }

    if (backdrop) backdrop.classList.add('active');
    try { document.body.style.overflow = 'hidden'; } catch(e) {}
  }

  function closeToolModal() {
    var backdrop = document.getElementById('toolModalBackdrop');
    if (backdrop) backdrop.classList.remove('active');
    try { document.body.style.overflow = ''; } catch(e) {}
  }

  // Build specific tool interactive forms
  function buildToolUI(tool) {
    switch (tool.id) {
      case 'img-compress':
        return `
          <div class="dropzone-box" onclick="document.getElementById('compressFileInput').click()">
            <input type="file" id="compressFileInput" accept="image/*" style="display:none;" onchange="handleCompressFile(this.files[0])"/>
            <div class="dropzone-icon"><i class="fas fa-cloud-arrow-up"></i></div>
            <div class="dropzone-text">
              <strong>Klik atau Drag & Drop foto di sini</strong>
              <span>Mendukung JPG, PNG, WebP</span>
            </div>
          </div>
          <div id="compressControlBox" style="display:none; flex-direction:column; gap:16px;">
            <div class="form-group">
              <label>Kualitas Kompresi: <span id="qualityValDisplay" style="color:var(--primary); font-weight:800;">80%</span></label>
              <input type="range" id="compressQualityRange" min="10" max="95" value="80" oninput="updateCompressQuality(this.value)" style="width:100%; accent-color:var(--primary);"/>
            </div>
            <div id="compressResultBox" class="output-card-box">
              <div class="output-header">
                <span>Hasil Kompresi</span>
                <span id="compressSizeBadge" style="color:#10b981; font-weight:800;"></span>
              </div>
              <div style="display:flex; justify-content:center; max-height:260px; overflow:hidden; border-radius:10px;">
                <img id="compressPreviewImg" style="max-width:100%; max-height:260px; object-fit:contain; border-radius:8px;"/>
              </div>
              <button class="btn-action-primary" id="downloadCompressedBtn" type="button">
                <i class="fas fa-download"></i> Unduh Foto Terkompres
              </button>
            </div>
          </div>
        `;

      case 'img-resize':
        return `
          <div class="dropzone-box" onclick="document.getElementById('resizeFileInput').click()">
            <input type="file" id="resizeFileInput" accept="image/*" style="display:none;" onchange="handleResizeFile(this.files[0])"/>
            <div class="dropzone-icon"><i class="fas fa-up-right-and-down-left-from-center"></i></div>
            <div class="dropzone-text"><strong>Pilih gambar yang ingin diubah ukurannya</strong></div>
          </div>
          <div id="resizeControls" style="display:none; flex-direction:column; gap:14px;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
              <div class="form-group">
                <label>Lebar (Pixel):</label>
                <input type="number" id="resizeWidthInput" class="form-input" oninput="handleDimensionChange('width')"/>
              </div>
              <div class="form-group">
                <label>Tinggi (Pixel):</label>
                <input type="number" id="resizeHeightInput" class="form-input" oninput="handleDimensionChange('height')"/>
              </div>
            </div>
            <label style="display:flex; align-items:center; gap:8px; font-size:12px; font-weight:700; cursor:pointer;">
              <input type="checkbox" id="lockAspectCheckbox" checked="checked"/> Kunci Rasio Aspek (Proporsional)
            </label>
            <button class="btn-action-primary" onclick="executeImageResize()" type="button"><i class="fas fa-check"></i> Proses & Unduh Hasil</button>
          </div>
        `;

      case 'qr-studio':
        return `
          <div class="form-group">
            <label>Konten / URL / Teks QR Code:</label>
            <input type="text" id="qrTextInput" class="form-input" placeholder="https://youtube.com/@saira54persena" value="https://saira54persena.blogspot.com"/>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
            <div class="form-group">
              <label>Warna QR:</label>
              <input type="color" id="qrFgColor" value="#0f172a" style="width:100%; height:40px; border-radius:8px; border:none; cursor:pointer;"/>
            </div>
            <div class="form-group">
              <label>Warna Latar:</label>
              <input type="color" id="qrBgColor" value="#ffffff" style="width:100%; height:40px; border-radius:8px; border:none; cursor:pointer;"/>
            </div>
          </div>
          <button class="btn-action-primary" onclick="generateQrCode()" type="button"><i class="fas fa-qrcode"></i> Buat QR Code</button>
          <div id="qrResultWrap" style="text-align:center; padding:16px; background:var(--bg-body); border-radius:14px; margin-top:10px;">
            <canvas id="qrCanvas" style="max-width:220px; border-radius:8px; box-shadow:var(--shadow-sm);"></canvas>
            <div style="margin-top:12px;">
              <button class="btn-action-secondary" onclick="downloadQrImage()" type="button"><i class="fas fa-download"></i> Unduh Gambar QR (PNG)</button>
            </div>
          </div>
        `;

      case 'css-gradient':
        return `
          <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
            <div class="form-group">
              <label>Warna Mulai:</label>
              <input type="color" id="gradColor1" value="#3b82f6" style="width:100%; height:38px; border:none; border-radius:8px; cursor:pointer;" onchange="updateGradientPreview()"/>
            </div>
            <div class="form-group">
              <label>Warna Akhir:</label>
              <input type="color" id="gradColor2" value="#ec4899" style="width:100%; height:38px; border:none; border-radius:8px; cursor:pointer;" onchange="updateGradientPreview()"/>
            </div>
            <div class="form-group">
              <label>Sudut (Deg): <span id="gradAngleText">135°</span></label>
              <input type="range" id="gradAngleRange" min="0" max="360" value="135" oninput="updateGradientPreview()" style="width:100%; accent-color:var(--primary);"/>
            </div>
          </div>
          <div id="gradPreviewBox" style="height:150px; border-radius:16px; box-shadow:var(--shadow-md); transition:background 0.2s;"></div>
          <div class="output-card-box">
            <div class="output-header">
              <span>Kode CSS</span>
              <button class="btn-action-secondary" onclick="copyToClipboard('gradCssCode')" style="padding:4px 10px; font-size:11px;" type="button"><i class="fas fa-copy"></i> Salin CSS</button>
            </div>
            <pre class="output-content-pre" id="gradCssCode">background: linear-gradient(135deg, #3b82f6, #ec4899);</pre>
          </div>
        `;

      case 'ai-prompt':
        return `
          <div class="form-group">
            <label>Ide Pokok / Konsep Singkat:</label>
            <input type="text" id="rawPromptInput" class="form-input" placeholder="Contoh: seekor kucing cyberpunk di malam hari"/>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
            <div class="form-group">
              <label>Gaya Visual:</label>
              <select id="promptStyleSelect" class="form-select">
                <option value="photorealistic">Fotorealistik 8K (Hyperrealistic Photography)</option>
                <option value="cinematic">Sinematik Film 35mm (Dramatic Lighting)</option>
                <option value="anime">Makoto Shinkai Anime (Vibrant Color)</option>
                <option value="cyberpunk">Cyberpunk Neon Sci-Fi (Volumetric Smoke)</option>
                <option value="octane">3D Octane Render (Unreal Engine 5)</option>
                <option value="watercolor">Lukisan Cat Air Masterpiece</option>
              </select>
            </div>
            <div class="form-group">
              <label>Pencahayaan & Suasana:</label>
              <select id="promptLightSelect" class="form-select">
                <option value="golden">Golden Hour Sunrays</option>
                <option value="neon">Moody Neon Cyber Glow</option>
                <option value="studio">Studio Softbox Commercial Light</option>
                <option value="dark">Dark Mysterious Shadow</option>
              </select>
            </div>
          </div>
          <button class="btn-action-primary" onclick="generateExpandedPrompt()" type="button"><i class="fas fa-wand-magic-sparkles"></i> Kembangkan Jadi Prompt Master</button>
          <div class="output-card-box" id="promptResultBox" style="display:none;">
            <div class="output-header">
              <span>Hasil Prompt Midjourney & ChatGPT:</span>
              <button class="btn-action-secondary" onclick="copyToClipboard('finalPromptResult')" style="padding:4px 10px; font-size:11px;" type="button"><i class="fas fa-copy"></i> Salin Prompt</button>
            </div>
            <pre class="output-content-pre" id="finalPromptResult"></pre>
          </div>
        `;

      case 'word-counter':
        return `
          <div class="form-group">
            <label>Ketik atau Tempelkan Teks di Sini:</label>
            <textarea id="wordCountTextarea" class="form-textarea" placeholder="Mulai mengetik atau tempelkan teks panjangmu di sini..." oninput="calculateWordStats()"></textarea>
          </div>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:10px;">
            <div class="output-card-box" style="text-align:center;">
              <span style="font-size:11px; color:var(--text-muted);">Jumlah Kata</span>
              <strong id="statWords" style="font-size:22px; color:var(--primary);">0</strong>
            </div>
            <div class="output-card-box" style="text-align:center;">
              <span style="font-size:11px; color:var(--text-muted);">Karakter (Spasi)</span>
              <strong id="statCharsWithSpace" style="font-size:22px; color:#8b5cf6;">0</strong>
            </div>
            <div class="output-card-box" style="text-align:center;">
              <span style="font-size:11px; color:var(--text-muted);">Karakter (No Spasi)</span>
              <strong id="statCharsNoSpace" style="font-size:22px; color:#ec4899;">0</strong>
            </div>
            <div class="output-card-box" style="text-align:center;">
              <span style="font-size:11px; color:var(--text-muted);">Waktu Baca</span>
              <strong id="statReadTime" style="font-size:20px; color:#10b981;">0 mnt</strong>
            </div>
          </div>
        `;

      case 'json-format':
        return `
          <div class="form-group">
            <label>Masukkan Data JSON:</label>
            <textarea id="jsonRawInput" class="form-textarea" placeholder='{"nama":"SAIRA 54PERSEN","status":"aktif","versi":1}'></textarea>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <button class="btn-action-primary" onclick="formatJsonData(2)" type="button"><i class="fas fa-indent"></i> Rapikan (Beautify 2-Spaces)</button>
            <button class="btn-action-secondary" onclick="formatJsonData(0)" type="button"><i class="fas fa-compress"></i> Minify (1 Baris)</button>
            <button class="btn-action-secondary" onclick="copyToClipboard('jsonRawInput')" type="button"><i class="fas fa-copy"></i> Salin JSON</button>
          </div>
          <div id="jsonErrorNotice" style="display:none; color:#ef4444; font-size:12px; font-weight:700; background:rgba(239,68,68,0.1); padding:8px 12px; border-radius:8px;"></div>
        `;

      case 'pass-gen':
        return `
          <div class="form-group">
            <label>Panjang Karakter: <span id="passLengthNum" style="color:var(--primary); font-weight:800;">16</span></label>
            <input type="range" id="passLengthRange" min="8" max="64" value="16" oninput="document.getElementById('passLengthNum').innerText=this.value; generatePassword();" style="width:100%; accent-color:var(--primary);"/>
          </div>
          <div style="display:flex; gap:16px; flex-wrap:wrap; font-size:12px; font-weight:700;">
            <label><input type="checkbox" id="passUpper" checked="checked" onchange="generatePassword()"/> Huruf Besar (A-Z)</label>
            <label><input type="checkbox" id="passLower" checked="checked" onchange="generatePassword()"/> Huruf Kecil (a-z)</label>
            <label><input type="checkbox" id="passNum" checked="checked" onchange="generatePassword()"/> Angka (0-9)</label>
            <label><input type="checkbox" id="passSym" checked="checked" onchange="generatePassword()"/> Simbol (!@#$%^&*)</label>
          </div>
          <div class="output-card-box" style="margin-top:14px;">
            <div class="output-header">
              <span>Kata Sandi Acak Kuat</span>
              <button class="btn-action-primary" onclick="copyToClipboard('generatedPassDisplay')" style="padding:4px 10px; font-size:11px;" type="button"><i class="fas fa-copy"></i> Salin Sandi</button>
            </div>
            <pre class="output-content-pre" id="generatedPassDisplay" style="font-size:16px; font-weight:700; color:var(--primary);"></pre>
          </div>
          <button class="btn-action-secondary" onclick="generatePassword()" type="button"><i class="fas fa-arrows-rotate"></i> Acak Ulang Sandi</button>
        `;

      case 'case-converter':
        return `
          <div class="form-group">
            <label>Masukkan Teks:</label>
            <textarea id="caseRawTextarea" class="form-textarea" placeholder="Tuliskan kalimat Anda di sini..."></textarea>
          </div>
          <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <button class="btn-action-secondary" onclick="convertTextCase('upper')" type="button">UPPERCASE</button>
            <button class="btn-action-secondary" onclick="convertTextCase('lower')" type="button">lowercase</button>
            <button class="btn-action-secondary" onclick="convertTextCase('title')" type="button">Title Case</button>
            <button class="btn-action-secondary" onclick="convertTextCase('camel')" type="button">camelCase</button>
            <button class="btn-action-secondary" onclick="convertTextCase('snake')" type="button">snake_case</button>
            <button class="btn-action-secondary" onclick="convertTextCase('kebab')" type="button">kebab-case</button>
          </div>
        `;

      case 'calc-discount':
        return `
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
            <div class="form-group">
              <label>Harga Asli (Rp):</label>
              <input type="number" id="discPriceInput" class="form-input" placeholder="Contoh: 150000" value="150000" oninput="calculateDiscount()"/>
            </div>
            <div class="form-group">
              <label>Diskon (%):</label>
              <input type="number" id="discPercentInput" class="form-input" placeholder="Contoh: 25" value="25" oninput="calculateDiscount()"/>
            </div>
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
            <div class="output-card-box" style="text-align:center;">
              <span style="font-size:11px; color:var(--text-muted);">Harga Setelah Diskon</span>
              <strong id="finalPriceDisplay" style="font-size:22px; color:#10b981;">Rp 112.500</strong>
            </div>
            <div class="output-card-box" style="text-align:center;">
              <span style="font-size:11px; color:var(--text-muted);">Total Anda Hemat</span>
              <strong id="savedPriceDisplay" style="font-size:22px; color:var(--primary);">Rp 37.500</strong>
            </div>
          </div>
        `;

      default:
        return `
          <div class="output-card-box" style="text-align:center; padding:30px;">
            <i class="${tool.icon}" style="font-size:40px; color:var(--primary); margin-bottom:12px;"></i>
            <h4 style="font-size:18px; margin-bottom:6px;">${tool.name}</h4>
            <p style="font-size:13px; color:var(--text-muted); margin-bottom:16px;">${tool.desc}</p>
            <div class="form-group">
              <textarea class="form-textarea" placeholder="Area kerja alat aktif..." id="genericInputBox"></textarea>
            </div>
            <div style="margin-top:12px;">
              <button class="btn-action-primary" onclick="alert('Alat ${tool.name} siap diproses!')" type="button"><i class="fas fa-play"></i> Jalankan Fungsi</button>
            </div>
          </div>
        `;
    }
  }

  // Logic handlers for tools
  function initToolLogic(toolId) {
    if (toolId === 'qr-studio') generateQrCode();
    if (toolId === 'css-gradient') updateGradientPreview();
    if (toolId === 'pass-gen') generatePassword();
    if (toolId === 'calc-discount') calculateDiscount();
  }

  // --- IMAGE COMPRESSOR LOGIC ---
  var currentCompressImg = null;
  function handleCompressFile(file) {
    if (!file) return;
    var reader = new FileReader();
    reader.onload = function(e) {
      var img = new Image();
      img.onload = function() {
        currentCompressImg = img;
        document.getElementById('compressControlBox').style.display = 'flex';
        processCompression();
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  function updateCompressQuality(val) {
    var d = document.getElementById('qualityValDisplay');
    if (d) d.innerText = val + '%';
    processCompression();
  }

  function processCompression() {
    if (!currentCompressImg) return;
    var quality = parseInt(document.getElementById('compressQualityRange').value) / 100;
    var canvas = document.createElement('canvas');
    canvas.width = currentCompressImg.width;
    canvas.height = currentCompressImg.height;
    var ctx = canvas.getContext('2d');
    ctx.drawImage(currentCompressImg, 0, 0);

    var dataUrl = canvas.toDataURL('image/jpeg', quality);
    var preview = document.getElementById('compressPreviewImg');
    if (preview) preview.src = dataUrl;

    var sizeKB = Math.round((dataUrl.length * 0.75) / 1024);
    var badge = document.getElementById('compressSizeBadge');
    if (badge) badge.innerText = sizeKB + ' KB';

    var dlBtn = document.getElementById('downloadCompressedBtn');
    if (dlBtn) {
      dlBtn.onclick = function() {
        var a = document.createElement('a');
        a.href = dataUrl;
        a.download = 'saira-compressed-' + Date.now() + '.jpg';
        a.click();
      };
    }
  }

  // --- QR CODE GENERATOR (NATIVE CANVAS) ---
  function generateQrCode() {
    var text = document.getElementById('qrTextInput').value.trim() || 'https://saira54persen.blogspot.com';
    var fg = document.getElementById('qrFgColor').value;
    var bg = document.getElementById('qrBgColor').value;
    var canvas = document.getElementById('qrCanvas');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    canvas.width = 240;
    canvas.height = 240;

    // Use free reliable QR API image on canvas for perfect QR Matrix
    var qrImg = new Image();
    qrImg.crossOrigin = 'anonymous';
    qrImg.onload = function() {
      ctx.fillStyle = bg;
      ctx.fillRect(0, 0, 240, 240);
      ctx.drawImage(qrImg, 15, 15, 210, 210);
    };
    qrImg.src = 'https://api.qrserver.com/v1/create-qr-code/?size=210x210&data=' + encodeURIComponent(text) + '&color=' + fg.replace('#','') + '&bgcolor=' + bg.replace('#','');
  }

  function downloadQrImage() {
    var canvas = document.getElementById('qrCanvas');
    if (!canvas) return;
    var a = document.createElement('a');
    a.href = canvas.toDataURL('image/png');
    a.download = 'saira-qrcode-' + Date.now() + '.png';
    a.click();
  }

  // --- GRADIENT GENERATOR ---
  function updateGradientPreview() {
    var c1 = document.getElementById('gradColor1').value;
    var c2 = document.getElementById('gradColor2').value;
    var deg = document.getElementById('gradAngleRange').value;
    var angleText = document.getElementById('gradAngleText');
    if (angleText) angleText.innerText = deg + '°';

    var css = 'linear-gradient(' + deg + 'deg, ' + c1 + ', ' + c2 + ')';
    var preview = document.getElementById('gradPreviewBox');
    if (preview) preview.style.background = css;

    var code = document.getElementById('gradCssCode');
    if (code) code.innerText = 'background: ' + css + ';';
  }

  // --- AI PROMPT EXPANDER ---
  function generateExpandedPrompt() {
    var raw = document.getElementById('rawPromptInput').value.trim();
    if (!raw) { alert('Silakan masukkan ide prompt singkat terlebih dahulu!'); return; }
    var style = document.getElementById('promptStyleSelect').value;
    var light = document.getElementById('promptLightSelect').value;

    var styleText = {
      photorealistic: '8k resolution, hyperrealistic photography, shot on Hasselblad H6D-100c, 85mm lens, f/1.8, extremely detailed skin and texture, award-winning national geographic shot',
      cinematic: 'cinematic still, 35mm film movie look, anamorphic lens flare, Panavision, masterpiece, IMAX cinematography, deep cinematic color grading',
      anime: 'Makoto Shinkai aesthetic, gorgeous anime key visual, Studio Ghibli inspired, vibrant saturated colors, breathtaking detailed sky and background, trending on Pixiv',
      cyberpunk: 'cyberpunk futuristic concept art, neon city reflections, volumetric fog, octane render, glowing holograms, high-tech dystopian atmosphere',
      octane: '3D digital render, Unreal Engine 5, Octane render, ray tracing global illumination, subsurface scattering, 3D masterwork, trending on ArtStation',
      watercolor: 'masterpiece watercolor painting, fluid ink washes, paper texture, elegant brushstrokes, artistic pastel palette, museum quality'
    }[style];

    var lightText = {
      golden: 'golden hour dramatic rim lighting, warm sunset atmosphere, soft volumetric god rays',
      neon: 'vivid neon lighting, ultraviolet reflections, cyan and magenta contrast, dark shadows',
      studio: 'professional three-point studio lighting, soft diffused bounce, pristine commercial clean',
      dark: 'chiaroscuro dramatic dark atmosphere, moody aesthetic, deep ambient shadows'
    }[light];

    var finalResult = raw + ', ' + styleText + ', ' + lightText + ', ultra-high definition, highly detailed, photorealistic, intricate masterpiece, --ar 16:9 --v 6.0 --q 2';
    var box = document.getElementById('promptResultBox');
    var resEl = document.getElementById('finalPromptResult');
    if (box) box.style.display = 'flex';
    if (resEl) resEl.innerText = finalResult;
  }

  // --- WORD COUNTER ---
  function calculateWordStats() {
    var text = document.getElementById('wordCountTextarea').value;
    var words = text.trim() ? text.trim().split(/\s+/).length : 0;
    var charsWithSpace = text.length;
    var charsNoSpace = text.replace(/\s/g, '').length;
    var readMins = Math.ceil(words / 200);

    document.getElementById('statWords').innerText = words;
    document.getElementById('statCharsWithSpace').innerText = charsWithSpace;
    document.getElementById('statCharsNoSpace').innerText = charsNoSpace;
    document.getElementById('statReadTime').innerText = (words > 0 ? readMins : 0) + ' mnt';
  }

  // --- JSON FORMATTER ---
  function formatJsonData(space) {
    var input = document.getElementById('jsonRawInput');
    var errNotice = document.getElementById('jsonErrorNotice');
    if (!input) return;
    try {
      var parsed = JSON.parse(input.value);
      input.value = JSON.stringify(parsed, null, space);
      if (errNotice) errNotice.style.display = 'none';
    } catch(e) {
      if (errNotice) {
        errNotice.style.display = 'block';
        errNotice.innerText = 'Error Sintaks JSON: ' + e.message;
      }
    }
  }

  // --- PASSWORD GENERATOR ---
  function generatePassword() {
    var len = parseInt(document.getElementById('passLengthRange').value) || 16;
    var upper = document.getElementById('passUpper').checked;
    var lower = document.getElementById('passLower').checked;
    var num = document.getElementById('passNum').checked;
    var sym = document.getElementById('passSym').checked;

    var chars = '';
    if (upper) chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (lower) chars += 'abcdefghijklmnopqrstuvwxyz';
    if (num) chars += '0123456789';
    if (sym) chars += '!@#$%^&*()_+-=[]{}|;:,.<>?';
    if (!chars) chars = 'abcdefghijklmnopqrstuvwxyz';

    var pass = '';
    for (var i = 0; i < len; i++) {
      pass += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    var disp = document.getElementById('generatedPassDisplay');
    if (disp) disp.innerText = pass;
  }

  // --- CASE CONVERTER ---
  function convertTextCase(type) {
    var el = document.getElementById('caseRawTextarea');
    if (!el) return;
    var val = el.value;
    switch(type) {
      case 'upper': el.value = val.toUpperCase(); break;
      case 'lower': el.value = val.toLowerCase(); break;
      case 'title':
        el.value = val.toLowerCase().replace(/\b\w/g, function(s) { return s.toUpperCase(); });
        break;
      case 'camel':
        el.value = val.toLowerCase().replace(/[^a-zA-Z0-9]+(.)/g, function(m, chr) { return chr.toUpperCase(); });
        break;
      case 'snake':
        el.value = val.toLowerCase().replace(/\s+/g, '_');
        break;
      case 'kebab':
        el.value = val.toLowerCase().replace(/\s+/g, '-');
        break;
    }
  }

  // --- DISCOUNT CALCULATOR ---
  function calculateDiscount() {
    var price = parseFloat(document.getElementById('discPriceInput').value) || 0;
    var percent = parseFloat(document.getElementById('discPercentInput').value) || 0;
    var saved = (price * percent) / 100;
    var finalPrice = price - saved;

    var fEl = document.getElementById('finalPriceDisplay');
    var sEl = document.getElementById('savedPriceDisplay');
    if (fEl) fEl.innerText = 'Rp ' + Math.round(finalPrice).toLocaleString('id-ID');
    if (sEl) sEl.innerText = 'Rp ' + Math.round(saved).toLocaleString('id-ID');
  }

  // --- COPY TO CLIPBOARD HELPER ---
  function copyToClipboard(elementId) {
    var el = document.getElementById(elementId);
    if (!el) return;
    var text = el.innerText || el.value;
    navigator.clipboard.writeText(text).then(function() {
      alert('Berhasil disalin ke Clipboard!');
    }).catch(function() {
      alert('Gagal menyalin otomatis, silakan salin manual.');
    });
  }

  // 5. GLOBAL UI CONTROLS & INITIALIZATION
  function toggleSidebar() {
    var isMobile = window.innerWidth <= 900;
    if (isMobile) {
      document.body.classList.toggle('sidebar-mobile-open');
      var backdrop = document.getElementById('sidebarBackdrop');
      if (backdrop) {
        if (document.body.classList.contains('sidebar-mobile-open')) {
          backdrop.classList.add('active');
        } else {
          backdrop.classList.remove('active');
        }
      }
    } else {
      document.body.classList.toggle('sidebar-collapsed');
    }
  }

  function toggleTheme() {
    document.body.classList.toggle('dark-theme');
    var icon = document.getElementById('themeIcon');
    if (document.body.classList.contains('dark-theme')) {
      if (icon) icon.className = 'fas fa-sun';
    } else {
      if (icon) icon.className = 'fas fa-moon';
    }
  }

  // Keyboard shortcut Ctrl + K for search
  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      var s = document.getElementById('globalSearchInput');
      if (s) { s.focus(); s.select(); }
    }
    if (e.key === 'Escape') closeToolModal();
  });

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Scroll Progress and Back-to-Top Listener
  window.addEventListener('scroll', function() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    var bar = document.getElementById('scrollProgressBar');
    if (bar) bar.style.width = scrolled + '%';

    var topBtn = document.getElementById('scrollToTopBtn');
    if (topBtn) {
      if (winScroll > 280) {
        topBtn.classList.add('visible');
      } else {
        topBtn.classList.remove('visible');
      }
    }
  });

  // Window onload initialization
  window.addEventListener('DOMContentLoaded', function() {
    renderToolsGrid(TOOLS_REGISTRY);
    updateFavBadgeCount();
  });
  //]]>
  </script>
</body>
</html>
"""

# 1. Write the Blogger XML file
with open(XML_OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(HTML_TEMPLATE.strip())

# 2. Generate standalone preview HTML
# Replace Blogger tags with standard HTML
preview_html = HTML_TEMPLATE
preview_html = preview_html.replace("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>", "<!DOCTYPE html>")
preview_html = preview_html.replace("<html b:css='false' b:defaultwidgetversion='2' b:layoutsversion='3' b:responsive='true' expr:dir='data:blog.languageDirection' lang='id' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>", "<html lang='id'>")
preview_html = preview_html.replace("<title><data:blog.pageTitle/></title>", "<title>SAIRA 54PERSEN AI TOOLS - Portal 1.000 Alat AI & Utilitas Online Gratis</title>")
preview_html = preview_html.replace("<b:include data='blog' name='all-head-content'/>", "")
preview_html = preview_html.replace("<b:skin><![CDATA[", "<style>")
preview_html = preview_html.replace("]]></b:skin>", "</style>")

# Remove blogger section
blogger_sec_pattern = re.compile(r"<b:section.*?</b:section>", re.DOTALL)
preview_html = blogger_sec_pattern.sub("", preview_html)

with open(PREVIEW_OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(preview_html.strip())

# 3. Validate XML
try:
    ET.parse(XML_OUTPUT_PATH)
    print("SUCCESS: saira-ai-tools-blogger.xml is 100% VALID XML!")
except Exception as e:
    print("ERROR parsing XML:", e)

print(f"SUCCESS: Generated:\n1. {XML_OUTPUT_PATH}\n2. {PREVIEW_OUTPUT_PATH}")
