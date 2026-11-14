import os
from PIL import Image, ImageDraw, ImageFont

UPLOAD_DIR = r"C:\Users\raval\.gemini\antigravity\brain\72862e93-721b-498f-9310-be17aba1770e\.user_uploaded"
OUT_DIR = r"C:\Users\raval\Documents\GitHub\ValtrixAI-Marketing\public\screenshots"

font_path = r"C:\Windows\Fonts\segoeui.ttf"
font_bold_path = r"C:\Windows\Fonts\segoeuib.ttf"
font_mono_path = r"C:\Windows\Fonts\consola.ttf"

def get_fonts():
    f_sm = ImageFont.truetype(font_path, 11)
    f_sm_b = ImageFont.truetype(font_bold_path, 11)
    f_md = ImageFont.truetype(font_path, 13)
    f_md_b = ImageFont.truetype(font_bold_path, 13)
    f_lg_b = ImageFont.truetype(font_bold_path, 16)
    f_xl_b = ImageFont.truetype(font_bold_path, 22)
    return f_sm, f_sm_b, f_md, f_md_b, f_lg_b, f_xl_b

f_sm, f_sm_b, f_md, f_md_b, f_lg_b, f_xl_b = get_fonts()

def apply_global_branding(img, draw):
    # 1. Rebrand Top-Left Logo (x: 4..130, y: 4..34)
    draw.rectangle([4, 4, 130, 34], fill=(255, 255, 255, 255))
    # Draw VQ emblem
    draw.polygon([(8, 8), (16, 28), (21, 16), (15, 8)], fill=(8, 119, 232, 255))
    draw.polygon([(16, 28), (19, 14), (21, 16)], fill=(8, 197, 232, 255))
    draw.polygon([(18, 8), (30, 8), (34, 16), (30, 24), (24, 24), (26, 16)], fill=(10, 37, 71, 255))
    draw.polygon([(25, 20), (32, 28), (35, 28), (28, 20)], fill=(8, 197, 232, 255))
    draw.text((38, 9), "VERIQON", fill=(6, 27, 54, 255), font=f_md_b)
    draw.text((96, 9), "ONE", fill=(8, 119, 232, 255), font=f_md_b)

    # 2. Rebrand Breadcrumbs in top bar (x: 145..360, y: 10..26)
    draw.rectangle([145, 10, 360, 26], fill=(255, 255, 255, 255))
    draw.text((148, 10), "VERIQON ONE", fill=(8, 119, 232, 255), font=f_sm_b)
    draw.text((226, 10), "/", fill=(148, 163, 184, 255), font=f_sm)
    draw.text((236, 10), "Production Workspace", fill=(71, 85, 105, 255), font=f_sm)
    draw.text((345, 10), "/", fill=(148, 163, 184, 255), font=f_sm)

    # 3. Rebrand bottom-left user email (x: 24..120, y: 458..482)
    draw.rectangle([24, 458, 120, 482], fill=(255, 255, 255, 255))
    draw.text((26, 460), "qa.lead@veriqon.com", fill=(30, 41, 59, 255), font=f_sm_b)
    draw.text((26, 471), "Enterprise Lead", fill=(100, 116, 139, 255), font=ImageFont.truetype(font_path, 9))

    # 4. Rebrand bottom footer status bar (x: 140..320, y: 488..502)
    draw.rectangle([140, 488, 320, 502], fill=(255, 255, 255, 255))
    draw.text((142, 489), "VERIQON ONE  |  Production Workspace  |  qa.lead@veriqon.com", fill=(100, 116, 139, 255), font=ImageFont.truetype(font_path, 9))


# 1. PROCESS DASHBOARD
def process_dashboard():
    src = os.path.join(UPLOAD_DIR, "media_1794674016241_20b52238.png")
    img = Image.open(src).convert("RGBA")
    draw = ImageDraw.Draw(img)
    apply_global_branding(img, draw)

    # Populate Lifecycle numbers
    # Step 1: 0 Tracked -> 48 Tracked
    draw.rectangle([165, 305, 225, 320], fill=(255, 255, 255, 255))
    draw.text((165, 306), "48 Tracked", fill=(30, 41, 59, 255), font=f_sm_b)

    # Step 2: 0 Generated -> 1,420 Generated
    draw.rectangle([330, 305, 415, 320], fill=(255, 255, 255, 255))
    draw.text((330, 306), "1,420 Generated", fill=(8, 119, 232, 255), font=f_sm_b)

    # Step 3: 0 Test Suites -> 56 Test Suites
    draw.rectangle([495, 305, 575, 320], fill=(255, 255, 255, 255))
    draw.text((495, 306), "56 Test Suites", fill=(16, 185, 129, 255), font=f_sm_b)

    # Step 4: Idle -> 12 Active Nodes
    draw.rectangle([658, 305, 735, 320], fill=(255, 255, 255, 255))
    draw.text((658, 306), "12 Active Nodes", fill=(245, 158, 11, 255), font=f_sm_b)

    # Step 5: 0% Pass Rate -> 99.8% Pass Rate
    draw.rectangle([820, 305, 915, 320], fill=(255, 255, 255, 255))
    draw.text((820, 306), "99.8% Pass Rate", fill=(16, 185, 129, 255), font=f_sm_b)

    out_path = os.path.join(OUT_DIR, "dashboard-console.png")
    img.save(out_path, "PNG")
    print("Dashboard saved to", out_path)

# 2. PROCESS EXECUTION CENTER
def process_execution_center():
    src = os.path.join(UPLOAD_DIR, "media_1794674250123_df1ba631.png")
    img = Image.open(src).convert("RGBA")
    draw = ImageDraw.Draw(img)
    apply_global_branding(img, draw)

    # Overwrite KPIs:
    # Executions: 0 -> 14,820
    draw.rectangle([165, 205, 215, 235], fill=(255, 255, 255, 255))
    draw.text((165, 206), "14,820", fill=(10, 37, 71, 255), font=f_lg_b)

    # Active Agents: 0 -> 12
    draw.rectangle([405, 205, 445, 235], fill=(255, 255, 255, 255))
    draw.text((405, 206), "12", fill=(8, 119, 232, 255), font=f_lg_b)

    # Schedules: 0 -> 8
    draw.rectangle([525, 205, 555, 235], fill=(255, 255, 255, 255))
    draw.text((525, 206), "8", fill=(10, 37, 71, 255), font=f_lg_b)

    # Passed: 0 -> 14,792
    draw.rectangle([645, 205, 695, 235], fill=(255, 255, 255, 255))
    draw.text((645, 206), "14,792", fill=(16, 185, 129, 255), font=f_lg_b)

    # Failed: 0 -> 28
    draw.rectangle([765, 205, 795, 235], fill=(255, 255, 255, 255))
    draw.text((765, 206), "28", fill=(239, 68, 68, 255), font=f_lg_b)

    # Pass Rate: 0% -> 99.81%
    draw.rectangle([880, 205, 935, 235], fill=(255, 255, 255, 255))
    draw.text((880, 206), "99.81%", fill=(16, 185, 129, 255), font=f_lg_b)

    # Overwrite Recent Unified Executions empty message with active rows!
    draw.rectangle([585, 340, 965, 460], fill=(255, 255, 255, 255))
    
    rows = [
        ("EXEC-8492", "Automation Studio", "Checkout Journey E2E (Chromium/WebKit)", "0.42s", "PASSED", (16, 185, 129)),
        ("EXEC-8491", "API Testing Studio", "Payment Gateway Contract Fuzzing", "0.08s", "PASSED", (16, 185, 129)),
        ("EXEC-8490", "ETL / Data Testing", "Snowflake Ledger Reconcile (1.2M rows)", "1.14s", "PASSED", (16, 185, 129)),
        ("EXEC-8489", "Security Studio", "PostgreSQL RLS Boundary Verification", "0.22s", "PASSED", (16, 185, 129)),
        ("EXEC-8488", "Performance Studio", "50,000 req/sec Peak Spike Simulation", "2.40s", "PASSED", (16, 185, 129))
    ]
    
    y = 345
    for r_id, studio, name, dur, status, color in rows:
        draw.rectangle([590, y, 960, y + 20], fill=(248, 250, 252, 255), outline=(226, 232, 240, 255))
        draw.text((596, y + 4), r_id, fill=(8, 119, 232, 255), font=f_sm_b)
        draw.text((665, y + 4), studio, fill=(10, 37, 71, 255), font=f_sm_b)
        draw.text((785, y + 4), name[:22], fill=(100, 116, 139, 255), font=f_sm)
        draw.text((900, y + 4), dur, fill=(148, 163, 184, 255), font=f_sm)
        draw.text((932, y + 4), status, fill=color, font=f_sm_b)
        y += 23

    out_path = os.path.join(OUT_DIR, "execution-center.png")
    img.save(out_path, "PNG")
    print("Execution Center saved to", out_path)

# 3. PROCESS TRACEABILITY & COVERAGE
def process_traceability():
    src = os.path.join(UPLOAD_DIR, "media_1794674224854_7143af43.png")
    img = Image.open(src).convert("RGBA")
    draw = ImageDraw.Draw(img)
    apply_global_branding(img, draw)

    # Overwrite Traceability Metrics:
    # Requirement Coverage: 0.0% -> 98.6%
    draw.rectangle([165, 395, 235, 435], fill=(255, 255, 255, 255))
    draw.text((165, 396), "98.6%", fill=(8, 119, 232, 255), font=f_xl_b)

    # User Story Coverage: 0.0% -> 99.2%
    draw.rectangle([375, 395, 445, 435], fill=(255, 255, 255, 255))
    draw.text((375, 396), "99.2%", fill=(8, 197, 232, 255), font=f_xl_b)

    # Traceability Integrity: 0% -> 100%
    draw.rectangle([585, 395, 655, 435], fill=(255, 255, 255, 255))
    draw.text((585, 396), "100%", fill=(16, 185, 129, 255), font=f_xl_b)

    # Uncovered Criteria Gaps: 0 Missing Test Links -> 0 Gaps (Resolved)
    draw.rectangle([795, 395, 960, 435], fill=(255, 255, 255, 255))
    draw.text((795, 396), "0", fill=(100, 116, 139, 255), font=f_xl_b)
    draw.text((818, 404), "Zero Gaps • AI Verified", fill=(16, 185, 129, 255), font=f_sm_b)

    out_path = os.path.join(OUT_DIR, "traceability-coverage.png")
    img.save(out_path, "PNG")
    print("Traceability saved to", out_path)

# 4. PROCESS ROLES & PERMISSIONS
def process_roles():
    src = os.path.join(UPLOAD_DIR, "media_1794674541429_1a9c7d2f.png")
    img = Image.open(src).convert("RGBA")
    draw = ImageDraw.Draw(img)
    apply_global_branding(img, draw)

    out_path = os.path.join(OUT_DIR, "roles-permissions.png")
    img.save(out_path, "PNG")
    print("Roles saved to", out_path)

# 5. PROCESS DEFECT MANAGEMENT
def process_defects():
    src = os.path.join(UPLOAD_DIR, "media_1794674127342_0db1ca1f.png")
    img = Image.open(src).convert("RGBA")
    draw = ImageDraw.Draw(img)
    apply_global_branding(img, draw)

    # Overwrite Defect Records (0) -> (14)
    draw.rectangle([155, 260, 310, 275], fill=(255, 255, 255, 255))
    draw.text((155, 260), "All Defect Records (14 Auto-Triaged)", fill=(71, 85, 105, 255), font=f_sm_b)

    # Replace empty table area with realistic self-healed and tracked defect records
    draw.rectangle([160, 290, 965, 465], fill=(255, 255, 255, 255))
    
    defects = [
        ("DEF-104", "HIGH", "Dynamic shadow-DOM selector drift on #pay-checkout", "Automation Studio", "AUTO-HEALED", (8, 197, 232)),
        ("DEF-103", "MEDIUM", "GraphQL schema nullability mismatch on /v2/ledger", "API Testing Studio", "RESOLVED", (16, 185, 129)),
        ("DEF-102", "CRITICAL", "Cross-tenant RLS boundary leakage probe", "Security Studio", "BLOCKED & SECURED", (16, 185, 129)),
        ("DEF-101", "LOW", "P99 Latency spike under 45k concurrent load", "Performance Studio", "ANALYZED", (245, 158, 11)),
        ("DEF-100", "MEDIUM", "Row hash drift on settlement ledger ingestion", "ETL / Data Studio", "VERIFIED", (16, 185, 129))
    ]
    
    y = 300
    for d_id, sev, title, studio, status, color in defects:
        draw.rectangle([170, y, 955, y + 26], fill=(248, 250, 252, 255), outline=(226, 232, 240, 255))
        draw.text((178, y + 6), d_id, fill=(8, 119, 232, 255), font=f_sm_b)
        draw.text((238, y + 6), sev, fill=(239, 68, 68, 255) if sev == "CRITICAL" else (10, 37, 71, 255), font=f_sm_b)
        draw.text((315, y + 6), title, fill=(30, 41, 59, 255), font=f_sm)
        draw.text((680, y + 6), studio, fill=(100, 116, 139, 255), font=f_sm)
        draw.text((840, y + 6), status, fill=color, font=f_sm_b)
        y += 30

    out_path = os.path.join(OUT_DIR, "defect-management.png")
    img.save(out_path, "PNG")
    print("Defects saved to", out_path)

# 6. PROCESS ANALYTICS & REPORTS
def process_analytics():
    src = os.path.join(UPLOAD_DIR, "media_1794674372804_0ffd0ed1.jpg")
    img = Image.open(src).convert("RGBA")
    draw = ImageDraw.Draw(img)
    apply_global_branding(img, draw)

    # Overwrite Not available cards
    # Quality Score: Not available -> 98.4 / 100
    draw.rectangle([155, 185, 250, 235], fill=(255, 255, 255, 255))
    draw.text((158, 192), "98.4 / 100", fill=(8, 119, 232, 255), font=f_lg_b)

    # Req Coverage: Not available -> 98.6%
    draw.rectangle([280, 185, 375, 235], fill=(255, 255, 255, 255))
    draw.text((283, 192), "98.6%", fill=(8, 197, 232, 255), font=f_lg_b)

    # Automation %: Not available -> 94.2%
    draw.rectangle([400, 185, 495, 235], fill=(255, 255, 255, 255))
    draw.text((403, 192), "94.2%", fill=(16, 185, 129, 255), font=f_lg_b)

    # Pass Rate: Not available -> 99.8%
    draw.rectangle([520, 185, 615, 235], fill=(255, 255, 255, 255))
    draw.text((523, 192), "99.8%", fill=(16, 185, 129, 255), font=f_lg_b)

    # AI Confidence: Not available -> 99.4%
    draw.rectangle([640, 185, 735, 235], fill=(255, 255, 255, 255))
    draw.text((643, 192), "99.4%", fill=(10, 37, 71, 255), font=f_lg_b)

    # Active Modules: Not available -> 7 Studios
    draw.rectangle([760, 185, 855, 235], fill=(255, 255, 255, 255))
    draw.text((763, 192), "7 Studios", fill=(8, 119, 232, 255), font=f_lg_b)

    out_path = os.path.join(OUT_DIR, "analytics-reports.png")
    img.save(out_path, "PNG")
    print("Analytics saved to", out_path)

# 7. PROCESS KNOWLEDGE HUB CONNECTORS
def process_knowledge():
    src = os.path.join(UPLOAD_DIR, "media_1794674389297_4a01bdce.png")
    img = Image.open(src).convert("RGBA")
    draw = ImageDraw.Draw(img)
    apply_global_branding(img, draw)

    # In Registered Connectors, replace "No connectors registered yet" with 4 live connectors
    draw.rectangle([435, 185, 960, 460], fill=(255, 255, 255, 255))
    
    connectors = [
        ("Jira Software Cloud", "42 Epics Ingested • Bi-directional Sync", "ACTIVE", (16, 185, 129)),
        ("Azure DevOps Repos", "124 User Stories • Work Item Sync", "ACTIVE", (16, 185, 129)),
        ("Confluence Enterprise", "8 Spaces • Architecture Specs", "ACTIVE", (16, 185, 129)),
        ("GitHub Enterprise CI", "Webhook HMAC SHA-256 Connected", "ACTIVE", (16, 185, 129))
    ]
    
    y = 200
    for name, desc, status, col in connectors:
        draw.rectangle([445, y, 950, y + 42], fill=(248, 250, 252, 255), outline=(226, 232, 240, 255))
        draw.text((460, y + 8), name, fill=(10, 37, 71, 255), font=f_md_b)
        draw.text((460, y + 24), desc, fill=(100, 116, 139, 255), font=f_sm)
        draw.text((890, y + 14), status, fill=col, font=f_sm_b)
        y += 54

    out_path = os.path.join(OUT_DIR, "knowledge-connectors.png")
    img.save(out_path, "PNG")
    print("Knowledge Connectors saved to", out_path)

if __name__ == "__main__":
    process_dashboard()
    process_execution_center()
    process_traceability()
    process_roles()
    process_defects()
    process_analytics()
    process_knowledge()
    print("ALL REAL SCREENSHOTS REBRANDED AND POPULATED SUCCESSFULLY!")
