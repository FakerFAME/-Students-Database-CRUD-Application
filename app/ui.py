"""
Dynamic, highly responsive HTML/CSS/JS dashboard for the Student Management System.
STRICT RESOLUTION: 1920x1080 (Full HD Command Center Architecture).
Features:
- Exact 1920x1080 native canvas with proportional auto-fit & 1:1 native toggle
- Zero page scroll; internal smooth-scrolling panels for cards and AI responses
- Glassmorphism dark aesthetic with ambient animated glowing mesh
- Real-time live status pulse & ticker
- Instant client-side & server-backed search & course filter tabs
- Interactive 'Professor Nova' AI Query Studio with streaming/markdown render & preset chips
- Full CRUD modals (Add Student, Edit Student, Delete with dynamic toasts)
"""

def get_dashboard_html() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1920, height=1080, initial-scale=1.0">
    <title>🎓 Nova Academy | Student Intelligence & CRUD Platform (1920x1080)</title>
    <!-- Modern Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <!-- Marked.js for rendering AI markdown responses -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        :root {
            --bg-base: #090d16;
            --bg-surface: rgba(17, 24, 39, 0.75);
            --bg-card: rgba(26, 34, 53, 0.65);
            --bg-card-hover: rgba(33, 44, 69, 0.85);
            --border-subtle: rgba(255, 255, 255, 0.08);
            --border-glow: rgba(99, 102, 241, 0.35);
            --primary: #6366f1;
            --primary-light: #818cf8;
            --secondary: #ec4899;
            --accent: #06b6d4;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --text-subtle: #64748b;
            --font-display: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
            --shadow-glow: 0 0 35px -5px rgba(99, 102, 241, 0.25);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            transition: border-color 0.2s, background-color 0.2s, color 0.2s;
        }

        /* Strict Full HD Root Container */
        html, body {
            width: 100vw;
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #05070d;
            color: var(--text-main);
            font-family: var(--font-body);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Ambient Animated Background Mesh */
        .ambient-mesh {
            position: absolute;
            top: 0;
            left: 0;
            width: 1920px;
            height: 1080px;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }

        .orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(120px);
            opacity: 0.28;
            animation: floatOrb 22s infinite alternate ease-in-out;
        }

        .orb-1 {
            top: -10%;
            left: 10%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, #6366f1 0%, transparent 70%);
        }

        .orb-2 {
            bottom: -15%;
            right: 5%;
            width: 650px;
            height: 650px;
            background: radial-gradient(circle, #ec4899 0%, transparent 70%);
            animation-duration: 28s;
            animation-direction: alternate-reverse;
        }

        .orb-3 {
            top: 40%;
            left: 45%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, #06b6d4 0%, transparent 70%);
            animation-duration: 18s;
        }

        @keyframes floatOrb {
            0% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(50px, 30px) scale(1.1); }
            100% { transform: translate(-30px, 60px) scale(0.95); }
        }

        /* Strict 1920x1080 Stage Viewport */
        #stage-canvas {
            width: 1920px;
            height: 1080px;
            min-width: 1920px;
            min-height: 1080px;
            max-width: 1920px;
            max-height: 1080px;
            position: relative;
            overflow: hidden;
            background: var(--bg-base);
            box-shadow: 0 0 60px rgba(0, 0, 0, 0.85);
            display: flex;
            flex-direction: column;
            padding: 20px 28px;
            z-index: 1;
        }

        /* Top Header */
        header {
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 24px;
            background: var(--bg-surface);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            margin-bottom: 16px;
            flex-shrink: 0;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }

        .brand-cluster {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .brand-icon {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: linear-gradient(135deg, #6366f1, #ec4899);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            box-shadow: 0 0 18px rgba(99, 102, 241, 0.4);
        }

        .brand-title {
            font-family: var(--font-display);
            font-size: 20px;
            font-weight: 700;
            background: linear-gradient(135deg, #fff 30%, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
            line-height: 1.2;
        }

        .brand-tag {
            font-size: 11px;
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 1.1px;
            font-weight: 600;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .res-badge {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 5px 12px;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 8px;
            font-family: var(--font-mono);
            font-size: 12px;
            font-weight: 600;
            color: var(--primary-light);
        }

        .pulse-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 5px 12px;
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 999px;
            font-size: 12px;
            font-weight: 600;
            color: #34d399;
        }

        .pulse-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #10b981;
            box-shadow: 0 0 10px #10b981;
            animation: pulseAnim 2s infinite;
        }

        @keyframes pulseAnim {
            0% { transform: scale(0.95); opacity: 0.7; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(0.95); opacity: 0.7; }
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 600;
            font-family: var(--font-body);
            border-radius: 10px;
            cursor: pointer;
            text-decoration: none;
            border: none;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .btn-gradient {
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.35);
        }

        .btn-gradient:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.06);
            color: var(--text-main);
            border: 1px solid var(--border-subtle);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.12);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-1px);
        }

        /* Metric Highlights Ribbon */
        .metrics-grid {
            height: 88px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-bottom: 16px;
            flex-shrink: 0;
        }

        .metric-card {
            background: var(--bg-surface);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 12px 18px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        }

        .metric-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .metric-label {
            font-size: 11px;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        .metric-icon-box {
            width: 28px;
            height: 28px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
            background: rgba(99, 102, 241, 0.15);
            color: var(--primary-light);
        }

        .metric-body {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
        }

        .metric-value {
            font-family: var(--font-display);
            font-size: 26px;
            font-weight: 700;
            color: #fff;
            letter-spacing: -0.5px;
            line-height: 1;
        }

        .metric-sub {
            font-size: 11px;
            color: var(--text-subtle);
        }

        .metric-sub .badge-pos {
            color: var(--success);
            font-weight: 600;
        }

        /* Workspace Grid (Fills remainder of 1080px) */
        .workspace-grid {
            flex: 1;
            min-height: 0; /* Critical for inner scrolling */
            display: grid;
            grid-template-columns: 1fr 500px;
            gap: 18px;
        }

        /* Panel Wrapper */
        .panel {
            background: var(--bg-surface);
            backdrop-filter: blur(16px);
            border: 1px solid var(--border-subtle);
            border-radius: 18px;
            padding: 18px 22px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25);
            display: flex;
            flex-direction: column;
            min-height: 0;
            overflow: hidden;
        }

        /* Left Panel Controls */
        .panel-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 14px;
            flex-shrink: 0;
        }

        .panel-title {
            font-family: var(--font-display);
            font-size: 18px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .search-strip {
            display: flex;
            gap: 12px;
            margin-bottom: 12px;
            flex-shrink: 0;
        }

        .search-box {
            position: relative;
            flex: 1;
        }

        .search-input {
            width: 100%;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 9px 16px 9px 38px;
            color: #fff;
            font-size: 13px;
            font-family: var(--font-body);
            outline: none;
        }

        .search-input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
            background: rgba(15, 23, 42, 0.9);
        }

        .search-icon {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 14px;
            color: var(--text-subtle);
            pointer-events: none;
        }

        /* Pills Bar */
        .pills-bar {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 8px;
            margin-bottom: 12px;
            flex-shrink: 0;
            scrollbar-width: thin;
        }

        .pill-tab {
            padding: 6px 12px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            font-size: 12px;
            font-weight: 500;
            color: var(--text-muted);
            cursor: pointer;
            white-space: nowrap;
        }

        .pill-tab:hover {
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
        }

        .pill-tab.active {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(139, 92, 246, 0.25));
            border-color: var(--primary);
            color: #fff;
            font-weight: 600;
        }

        /* Students Cards Grid */
        .students-deck {
            flex: 1;
            min-height: 0;
            overflow-y: auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            padding-right: 6px;
            scrollbar-width: thin;
            scrollbar-color: rgba(99, 102, 241, 0.3) transparent;
        }

        .students-deck::-webkit-scrollbar {
            width: 6px;
        }
        .students-deck::-webkit-scrollbar-thumb {
            background: rgba(99, 102, 241, 0.3);
            border-radius: 10px;
        }

        .student-card {
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            height: 200px;
        }

        .student-card:hover {
            border-color: var(--border-glow);
            background: var(--bg-card-hover);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }

        .card-top {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 10px;
        }

        .avatar-initials {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-display);
            font-weight: 700;
            font-size: 15px;
            color: #fff;
            flex-shrink: 0;
        }

        .student-meta {
            flex: 1;
            min-width: 0;
        }

        .student-name {
            font-family: var(--font-display);
            font-size: 15px;
            font-weight: 700;
            color: #fff;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            margin-bottom: 2px;
        }

        .course-tag {
            display: inline-block;
            font-size: 10px;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 6px;
            background: rgba(99, 102, 241, 0.15);
            color: var(--primary-light);
            border: 1px solid rgba(99, 102, 241, 0.3);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 100%;
        }

        .card-details {
            display: flex;
            flex-direction: column;
            gap: 5px;
            font-size: 11px;
            color: var(--text-muted);
            margin-bottom: 10px;
        }

        .detail-row {
            display: flex;
            align-items: center;
            gap: 8px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .detail-icon {
            font-size: 12px;
            color: var(--text-subtle);
            flex-shrink: 0;
        }

        .card-actions {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 10px;
            border-top: 1px solid var(--border-subtle);
        }

        .id-badge {
            font-family: var(--font-mono);
            font-size: 11px;
            color: var(--text-subtle);
        }

        .action-btns {
            display: flex;
            gap: 6px;
        }

        .btn-icon-sm {
            width: 28px;
            height: 28px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            border: 1px solid var(--border-subtle);
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-muted);
            font-size: 12px;
        }

        .btn-icon-sm:hover {
            color: #fff;
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255, 255, 255, 0.3);
        }

        .btn-icon-sm.delete:hover {
            background: rgba(239, 68, 68, 0.2);
            border-color: var(--danger);
            color: #fca5a5;
        }

        /* Right Panel: Professor Nova AI Studio */
        .ai-banner {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(236, 72, 153, 0.15));
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 12px;
            padding: 10px 14px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            flex-shrink: 0;
        }

        .ai-avatar {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            background: linear-gradient(135deg, #8b5cf6, #ec4899);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            box-shadow: 0 0 15px rgba(236, 72, 153, 0.4);
        }

        .ai-banner-text h4 {
            font-family: var(--font-display);
            font-size: 14px;
            color: #fff;
        }

        .ai-banner-text p {
            font-size: 11px;
            color: var(--text-muted);
        }

        .prompt-presets {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 12px;
            flex-shrink: 0;
        }

        .preset-title {
            font-size: 11px;
            color: var(--text-subtle);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        .preset-chip {
            padding: 7px 12px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            font-size: 12px;
            color: #cbd5e1;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .preset-chip:hover {
            background: rgba(99, 102, 241, 0.12);
            border-color: var(--primary-light);
            color: #fff;
            transform: translateX(3px);
        }

        .ai-query-form {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 12px;
            flex-shrink: 0;
        }

        .ai-textarea {
            width: 100%;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--border-subtle);
            border-radius: 10px;
            padding: 10px 14px;
            color: #fff;
            font-family: var(--font-body);
            font-size: 13px;
            resize: none;
            outline: none;
            height: 64px;
        }

        .ai-textarea:focus {
            border-color: var(--secondary);
            box-shadow: 0 0 0 3px rgba(236, 72, 153, 0.2);
        }

        .btn-ai-submit {
            background: linear-gradient(135deg, #ec4899, #8b5cf6);
            color: #fff;
            font-weight: 700;
            padding: 8px 14px;
            font-size: 13px;
            box-shadow: 0 4px 18px rgba(236, 72, 153, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn-ai-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(236, 72, 153, 0.5);
        }

        /* AI Output Box - Scrollable Inside 1080px */
        .ai-output-box {
            flex: 1;
            min-height: 0;
            overflow-y: auto;
            background: rgba(10, 15, 28, 0.85);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 16px;
            font-size: 13px;
            line-height: 1.5;
            color: #e2e8f0;
            scrollbar-width: thin;
            scrollbar-color: rgba(236, 72, 153, 0.3) transparent;
        }

        .ai-output-box::-webkit-scrollbar {
            width: 6px;
        }
        .ai-output-box::-webkit-scrollbar-thumb {
            background: rgba(236, 72, 153, 0.3);
            border-radius: 10px;
        }

        .ai-output-box h3, .ai-output-box h4 {
            color: #fff;
            margin: 8px 0 6px;
            font-family: var(--font-display);
        }

        .ai-output-box ul {
            padding-left: 18px;
            margin-bottom: 8px;
        }

        .ai-output-box li {
            margin-bottom: 4px;
        }

        .ai-output-box strong {
            color: #67e8f9;
        }

        .ai-output-meta {
            margin-top: 12px;
            padding-top: 10px;
            border-top: 1px solid var(--border-subtle);
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 11px;
            color: var(--text-subtle);
            font-family: var(--font-mono);
        }

        /* Modals & Toasts */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 1920px;
            height: 1080px;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(8px);
            z-index: 1000;
            display: none;
            align-items: center;
            justify-content: center;
        }

        .modal-overlay.active {
            display: flex;
        }

        .modal-card {
            background: #111827;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            width: 520px;
            padding: 28px;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
        }

        .modal-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .modal-title {
            font-family: var(--font-display);
            font-size: 20px;
            font-weight: 700;
            color: #fff;
        }

        .modal-close {
            background: none;
            border: none;
            color: var(--text-subtle);
            font-size: 20px;
            cursor: pointer;
        }

        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
            margin-bottom: 20px;
        }

        .form-group-full {
            grid-column: span 2;
        }

        .form-label {
            display: block;
            font-size: 11px;
            font-weight: 600;
            color: var(--text-muted);
            margin-bottom: 5px;
            text-transform: uppercase;
        }

        .form-input {
            width: 100%;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid var(--border-subtle);
            border-radius: 8px;
            padding: 9px 12px;
            color: #fff;
            font-size: 13px;
            outline: none;
        }

        .toast-container {
            position: absolute;
            bottom: 28px;
            right: 28px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 10px;
            pointer-events: none;
        }

        .toast {
            pointer-events: auto;
            background: #1e293b;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 18px;
            color: #fff;
            font-size: 13px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .toast.success { border-left: 4px solid var(--success); }
        .toast.error { border-left: 4px solid var(--danger); }
        .toast.info { border-left: 4px solid var(--accent); }

        .empty-state {
            grid-column: 1 / -1;
            text-align: center;
            padding: 50px 20px;
            color: var(--text-subtle);
        }
    </style>
</head>
<body>

    <!-- Strict 1920x1080 Stage Viewport Canvas -->
    <div id="stage-canvas">
        <!-- Ambient Animated Glow Orbs -->
        <div class="ambient-mesh">
            <div class="orb orb-1"></div>
            <div class="orb orb-2"></div>
            <div class="orb orb-3"></div>
        </div>

        <!-- 1. Header (Fixed 64px) -->
        <header>
            <div class="brand-cluster">
                <div class="brand-icon">🎓</div>
                <div>
                    <div class="brand-title">Nova Academy</div>
                    <div class="brand-tag">Student Intelligence & Registry Platform</div>
                </div>
            </div>
            <div class="header-actions">
                <div class="res-badge">
                    <span>🖥️ 1920 × 1080 FHD</span>
                </div>
                <div class="pulse-badge">
                    <div class="pulse-dot"></div>
                    <span id="server-ping-text">FastAPI 0.143 Live</span>
                </div>
                <button class="btn btn-secondary" onclick="toggleScaling()" id="scaleToggleBtn" title="Toggle Auto-Fit vs Strict 1:1 Scale">
                    <span>⛶ Auto-Fit Scale</span>
                </button>
                <a href="/docs" target="_blank" class="btn btn-secondary">
                    <span>📖 Swagger API Docs</span>
                </a>
                <button class="btn btn-gradient" onclick="openCreateModal()">
                    <span>+ Enrol Student</span>
                </button>
            </div>
        </header>

        <!-- 2. Metrics Ribbon (Fixed 88px) -->
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-header">
                    <span class="metric-label">Enrolled Scholars</span>
                    <div class="metric-icon-box">👥</div>
                </div>
                <div class="metric-body">
                    <div class="metric-value" id="stat-total-students">0</div>
                    <div class="metric-sub"><span class="badge-pos">● SQLite Database</span> active</div>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <span class="metric-label">Active Programs</span>
                    <div class="metric-icon-box">🏛️</div>
                </div>
                <div class="metric-body">
                    <div class="metric-value" id="stat-total-courses">0</div>
                    <div class="metric-sub"><span>STEM tracks indexed</span></div>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <span class="metric-label">AI Neural Engine</span>
                    <div class="metric-icon-box">⚡</div>
                </div>
                <div class="metric-body">
                    <div class="metric-value" style="font-size: 20px;">Gemini 3.8 Flash</div>
                    <div class="metric-sub"><span class="badge-pos">● Grounded</span> reasoning</div>
                </div>
            </div>

            <div class="metric-card">
                <div class="metric-header">
                    <span class="metric-label">System Latency</span>
                    <div class="metric-icon-box">⏱️</div>
                </div>
                <div class="metric-body">
                    <div class="metric-value" id="stat-latency">&lt; 10ms</div>
                    <div class="metric-sub"><span class="badge-pos">● ASGI Engine</span> responsive</div>
                </div>
            </div>
        </div>

        <!-- 3. Workspace Grid (Fills Remaining 844px without window scroll) -->
        <div class="workspace-grid">
            <!-- Left: Student Registry (3-column scrollable grid) -->
            <div class="panel">
                <div class="panel-header">
                    <div class="panel-title">
                        <span>📋 Student Registry</span>
                        <span id="filtered-count-badge" style="font-size: 12px; font-weight: 600; padding: 2px 8px; background: rgba(255,255,255,0.08); border-radius: 999px; color: var(--accent);">0 records</span>
                    </div>
                    <div>
                        <button class="btn btn-secondary" onclick="fetchStudents()" style="padding: 6px 12px; font-size: 12px;">
                            <span>↺ Refresh</span>
                        </button>
                    </div>
                </div>

                <div class="search-strip">
                    <div class="search-box">
                        <span class="search-icon">🔍</span>
                        <input type="text" id="searchInput" class="search-input" placeholder="Search by name, email, course, or city..." oninput="handleSearch()">
                    </div>
                </div>

                <div class="pills-bar" id="coursePills">
                    <div class="pill-tab active" onclick="setFilter('ALL')">All Tracks</div>
                </div>

                <div class="students-deck" id="studentsDeck">
                    <!-- Cards populated dynamically -->
                </div>
            </div>

            <!-- Right: Professor Nova AI Studio -->
            <div class="panel">
                <div class="ai-banner">
                    <div class="ai-avatar">✨</div>
                    <div class="ai-banner-text">
                        <h4>Professor Nova AI</h4>
                        <p>Natural Language Academic Advisor</p>
                    </div>
                </div>

                <div class="prompt-presets">
                    <div class="preset-title">Suggested Inquiries</div>
                    <div class="preset-chip" onclick="askPreset('Which students are enrolled in Quantum Computing & AI?')">
                        <span>⚛️ Who studies Quantum Computing?</span>
                        <span style="color: var(--primary-light);">→</span>
                    </div>
                    <div class="preset-chip" onclick="askPreset('Give me an overview of all enrolled students.')">
                        <span>📊 Full cohort demographic breakdown</span>
                        <span style="color: var(--primary-light);">→</span>
                    </div>
                    <div class="preset-chip" onclick="askPreset('Who are the students located in Cambridge or Seattle?')">
                        <span>📍 Geographic campus directory</span>
                        <span style="color: var(--primary-light);">→</span>
                    </div>
                </div>

                <form class="ai-query-form" onsubmit="handleAIQuery(event)">
                    <textarea id="aiQuestionInput" class="ai-textarea" placeholder="Ask anything about students, courses, enrollment dates, or locations..."></textarea>
                    <button type="submit" id="aiSubmitBtn" class="btn btn-ai-submit">
                        <span id="aiBtnText">✨ Consult Advisor</span>
                    </button>
                </form>

                <div class="ai-output-box" id="aiOutputBox">
                    <div style="text-align: center; color: var(--text-subtle); padding: 30px 10px;">
                        <div style="font-size: 28px; margin-bottom: 8px;">💬</div>
                        <p>Ask a question above or choose a preset.</p>
                        <p style="font-size: 11px; margin-top: 4px;">Grounded with Gemini 3.8 Flash & SQLite</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modals & Toasts -->
        <div class="modal-overlay" id="studentModal">
            <div class="modal-card">
                <div class="modal-header">
                    <div class="modal-title" id="modalTitle">Enrol New Student</div>
                    <button class="modal-close" onclick="closeStudentModal()">&times;</button>
                </div>
                <form id="studentForm" onsubmit="handleSaveStudent(event)">
                    <input type="hidden" id="studentIdInput">
                    <div class="form-grid">
                        <div class="form-group-full">
                            <label class="form-label">Full Name *</label>
                            <input type="text" id="nameInput" class="form-input" required placeholder="Aria Chen">
                        </div>
                        <div>
                            <label class="form-label">Date of Birth *</label>
                            <input type="date" id="dobInput" class="form-input" required>
                        </div>
                        <div>
                            <label class="form-label">Enrollment Date</label>
                            <input type="date" id="enrollmentInput" class="form-input">
                        </div>
                        <div class="form-group-full">
                            <label class="form-label">Email Address *</label>
                            <input type="email" id="emailInput" class="form-input" required placeholder="aria.chen@nexus.edu">
                        </div>
                        <div>
                            <label class="form-label">Phone Number *</label>
                            <input type="text" id="phoneInput" class="form-input" required placeholder="+1-415-555-0199">
                        </div>
                        <div>
                            <label class="form-label">Academic Program</label>
                            <input type="text" id="courseInput" class="form-input" placeholder="Quantum Computing & AI">
                        </div>
                        <div class="form-group-full">
                            <label class="form-label">Campus Address</label>
                            <input type="text" id="addressInput" class="form-input" placeholder="Suite 404, Cambridge">
                        </div>
                    </div>
                    <div style="display: flex; justify-content: flex-end; gap: 10px;">
                        <button type="button" class="btn btn-secondary" onclick="closeStudentModal()">Cancel</button>
                        <button type="submit" class="btn btn-gradient">Save Record</button>
                    </div>
                </form>
            </div>
        </div>

        <div class="toast-container" id="toastContainer"></div>
    </div>

    <script>
        // Strict 1920x1080 Viewport Auto-Scaling Engine
        let autoFitEnabled = true;

        function applyStageScaling() {
            const stage = document.getElementById('stage-canvas');
            if (!stage) return;

            if (autoFitEnabled) {
                const scaleX = window.innerWidth / 1920;
                const scaleY = window.innerHeight / 1080;
                const scale = Math.min(scaleX, scaleY);
                stage.style.transform = `scale(${scale})`;
                stage.style.transformOrigin = 'center center';
            } else {
                stage.style.transform = 'none';
            }
        }

        function toggleScaling() {
            autoFitEnabled = !autoFitEnabled;
            const btn = document.getElementById('scaleToggleBtn');
            btn.innerHTML = autoFitEnabled ? '<span>⛶ Auto-Fit Scale</span>' : '<span>🖥️ Strict 1:1 Scale</span>';
            applyStageScaling();
        }

        window.addEventListener('resize', applyStageScaling);
        window.addEventListener('DOMContentLoaded', () => {
            applyStageScaling();
            fetchStudents();
        });

        // Data State
        let allStudents = [];
        let activeCourseFilter = 'ALL';
        const colorPalette = [
            'linear-gradient(135deg, #6366f1, #8b5cf6)',
            'linear-gradient(135deg, #ec4899, #f43f5e)',
            'linear-gradient(135deg, #06b6d4, #3b82f6)',
            'linear-gradient(135deg, #10b981, #059669)',
            'linear-gradient(135deg, #f59e0b, #d97706)',
            'linear-gradient(135deg, #8b5cf6, #d946ef)'
        ];

        function getAvatarColor(id) {
            return colorPalette[(id || 0) % colorPalette.length];
        }

        function getInitials(name) {
            if (!name) return '??';
            const parts = name.trim().split(' ');
            if (parts.length === 1) return parts[0].substring(0, 2).toUpperCase();
            return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
        }

        function showToast(message, type = 'info') {
            const container = document.getElementById('toastContainer');
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            const icon = type === 'success' ? '✅' : type === 'error' ? '❌' : 'ℹ️';
            toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
            container.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(50px)';
                toast.style.transition = 'all 0.3s ease';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        async function fetchStudents() {
            const t0 = performance.now();
            try {
                const response = await fetch('/students/');
                if (!response.ok) throw new Error('Failed to load students');
                allStudents = await response.json();
                const latency = Math.round(performance.now() - t0);
                document.getElementById('stat-latency').innerText = `${latency} ms`;
                renderMetrics();
                renderCoursePills();
                renderStudents();
            } catch (err) {
                showToast(err.message, 'error');
            }
        }

        function renderMetrics() {
            document.getElementById('stat-total-students').innerText = allStudents.length;
            const courses = new Set(allStudents.map(s => s.course).filter(Boolean));
            document.getElementById('stat-total-courses').innerText = courses.size;
        }

        function renderCoursePills() {
            const container = document.getElementById('coursePills');
            const courses = Array.from(new Set(allStudents.map(s => s.course).filter(Boolean)));
            
            let html = `<div class="pill-tab ${activeCourseFilter === 'ALL' ? 'active' : ''}" onclick="setFilter('ALL')">All Tracks (${allStudents.length})</div>`;
            courses.forEach(c => {
                const count = allStudents.filter(s => s.course === c).length;
                html += `<div class="pill-tab ${activeCourseFilter === c ? 'active' : ''}" onclick="setFilter('${c}')">${c} (${count})</div>`;
            });
            container.innerHTML = html;
        }

        function setFilter(course) {
            activeCourseFilter = course;
            renderCoursePills();
            renderStudents();
        }

        function handleSearch() {
            renderStudents();
        }

        function renderStudents() {
            const query = (document.getElementById('searchInput').value || '').toLowerCase().trim();
            const deck = document.getElementById('studentsDeck');

            let filtered = allStudents.filter(s => {
                const matchesCourse = activeCourseFilter === 'ALL' || s.course === activeCourseFilter;
                const matchesSearch = !query || 
                    (s.student_name && s.student_name.toLowerCase().includes(query)) ||
                    (s.email && s.email.toLowerCase().includes(query)) ||
                    (s.course && s.course.toLowerCase().includes(query)) ||
                    (s.address && s.address.toLowerCase().includes(query));
                return matchesCourse && matchesSearch;
            });

            document.getElementById('filtered-count-badge').innerText = `${filtered.length} record${filtered.length === 1 ? '' : 's'}`;

            if (filtered.length === 0) {
                deck.innerHTML = `
                    <div class="empty-state">
                        <div style="font-size: 32px; margin-bottom: 8px;">🔍</div>
                        <h4>No matching records</h4>
                        <p style="font-size: 12px; margin-top: 4px;">Try a different keyword or category.</p>
                    </div>
                `;
                return;
            }

            deck.innerHTML = filtered.map(s => `
                <div class="student-card">
                    <div>
                        <div class="card-top">
                            <div class="avatar-initials" style="background: ${getAvatarColor(s.id)};">
                                ${getInitials(s.student_name)}
                            </div>
                            <div class="student-meta">
                                <div class="student-name" title="${s.student_name}">${s.student_name}</div>
                                <span class="course-tag" title="${s.course || 'Undeclared'}">${s.course || 'General Studies'}</span>
                            </div>
                        </div>

                        <div class="card-details">
                            <div class="detail-row" title="${s.email}">
                                <span class="detail-icon">✉️</span>
                                <span>${s.email}</span>
                            </div>
                            <div class="detail-row" title="${s.phone}">
                                <span class="detail-icon">📞</span>
                                <span>${s.phone}</span>
                            </div>
                            <div class="detail-row" title="${s.address || 'Campus Base'}">
                                <span class="detail-icon">📍</span>
                                <span>${s.address || 'Campus Base'}</span>
                            </div>
                            <div class="detail-row" title="${s.enrollment_date || 'N/A'}">
                                <span class="detail-icon">📅</span>
                                <span>Enrolled: ${s.enrollment_date || 'N/A'}</span>
                            </div>
                        </div>
                    </div>

                    <div class="card-actions">
                        <span class="id-badge">ID #${s.id}</span>
                        <div class="action-btns">
                            <button class="btn-icon-sm" title="Edit scholar" onclick="openEditModal(${s.id})">✏️</button>
                            <button class="btn-icon-sm delete" title="Delete record" onclick="deleteStudent(${s.id}, '${s.student_name.replace(/'/g, "\\'")}')">🗑️</button>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        // CRUD Modals
        function openCreateModal() {
            document.getElementById('modalTitle').innerText = 'Enrol New Scholar';
            document.getElementById('studentIdInput').value = '';
            document.getElementById('studentForm').reset();
            document.getElementById('studentModal').classList.add('active');
        }

        function openEditModal(id) {
            const student = allStudents.find(s => s.id === id);
            if (!student) return;

            document.getElementById('modalTitle').innerText = `Update Scholar: ${student.student_name}`;
            document.getElementById('studentIdInput').value = student.id;
            document.getElementById('nameInput').value = student.student_name || '';
            document.getElementById('dobInput').value = student.date_of_birth || '';
            document.getElementById('enrollmentInput').value = student.enrollment_date || '';
            document.getElementById('emailInput').value = student.email || '';
            document.getElementById('phoneInput').value = student.phone || '';
            document.getElementById('courseInput').value = student.course || '';
            document.getElementById('addressInput').value = student.address || '';
            document.getElementById('studentModal').classList.add('active');
        }

        function closeStudentModal() {
            document.getElementById('studentModal').classList.remove('active');
        }

        async function handleSaveStudent(e) {
            e.preventDefault();
            const id = document.getElementById('studentIdInput').value;
            const payload = {
                student_name: document.getElementById('nameInput').value.trim(),
                date_of_birth: document.getElementById('dobInput').value,
                enrollment_date: document.getElementById('enrollmentInput').value || null,
                email: document.getElementById('emailInput').value.trim(),
                phone: document.getElementById('phoneInput').value.trim(),
                course: document.getElementById('courseInput').value.trim() || null,
                address: document.getElementById('addressInput').value.trim() || null
            };

            try {
                let response;
                if (id) {
                    response = await fetch(`/students/${id}`, {
                        method: 'PUT',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                } else {
                    response = await fetch('/students/', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                }

                if (!response.ok) {
                    const errData = await response.json();
                    throw new Error(errData.detail || 'Could not save student record');
                }

                closeStudentModal();
                showToast(id ? 'Record updated successfully! 🚀' : 'Scholar enrolled successfully! 🎉', 'success');
                fetchStudents();
            } catch (err) {
                showToast(err.message, 'error');
            }
        }

        async function deleteStudent(id, name) {
            if (!confirm(`Are you sure you want to remove ${name} (ID #${id}) from the registry?`)) return;

            try {
                const response = await fetch(`/students/${id}`, { method: 'DELETE' });
                if (!response.ok) {
                    const err = await response.json();
                    throw new Error(err.detail || 'Failed to delete student');
                }
                showToast(`Removed ${name} from registry.`, 'info');
                fetchStudents();
            } catch (err) {
                showToast(err.message, 'error');
            }
        }

        // AI Studio
        function askPreset(question) {
            document.getElementById('aiQuestionInput').value = question;
            handleAIQuery();
        }

        async function handleAIQuery(e) {
            if (e) e.preventDefault();
            const input = document.getElementById('aiQuestionInput');
            const question = input.value.trim();
            if (!question) return;

            const box = document.getElementById('aiOutputBox');
            const btn = document.getElementById('aiSubmitBtn');
            const btnText = document.getElementById('aiBtnText');

            btn.disabled = true;
            btnText.innerText = 'Synthesizing...';

            box.innerHTML = `
                <div style="padding: 10px 0; color: var(--accent);">
                    <div style="font-size: 13px; margin-bottom: 8px;">⚡ Consulting registry with Gemini 3.8 Flash...</div>
                    <div style="height: 12px; background: rgba(255,255,255,0.1); border-radius: 6px; width: 85%;"></div>
                </div>
            `;

            try {
                const response = await fetch('/students/ai-query/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question })
                });

                if (!response.ok) {
                    const err = await response.json();
                    throw new Error(err.detail || 'AI Reasoning service error');
                }

                const data = await response.json();
                const parsedMarkdown = typeof marked !== 'undefined' ? marked.parse(data.answer) : data.answer;

                box.innerHTML = `
                    <div style="color: #f1f5f9;">
                        ${parsedMarkdown}
                    </div>
                    <div class="ai-output-meta">
                        <span>⚡ Latency: ${data.execution_time_ms ? data.execution_time_ms + 'ms' : 'Fast'}</span>
                        <span>📊 ${data.records_considered} records evaluated</span>
                        <span>🤖 ${data.model_name || 'Gemini 3.8 Flash'}</span>
                    </div>
                `;
                showToast('Intelligence synthesis complete! ✨', 'success');
            } catch (err) {
                box.innerHTML = `
                    <div style="color: #f87171; padding: 10px 0;">
                        <h4>⚠️ Intelligence Query Notice</h4>
                        <p style="margin-top: 6px; font-size: 12px;">${err.message}</p>
                    </div>
                `;
                showToast(err.message, 'error');
            } finally {
                btn.disabled = false;
                btnText.innerText = '✨ Consult Advisor';
            }
        }
    </script>
</body>
</html>
"""
