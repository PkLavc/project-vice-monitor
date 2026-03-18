#!/usr/bin/env python3
"""
Script para gerar dados de teste para o blog do Project Vice Monitor
"""

import os
import json
import datetime
import random

def generate_test_blog_entries():
    """Gera entradas de blog de teste"""
    
    # Cria diretório blog se não existir
    if not os.path.exists('blog'):
        os.makedirs('blog')
    
    # Dados de teste
    test_entries = [
        {
            "timestamp": "2026-03-15T10:30:00+00:00",
            "service": {
                "name": "GTA VI Official",
                "url": "https://www.rockstargames.com/VI/",
                "keywords": ["Grand Theft Auto", "GTA VI", "Rockstar"]
            },
            "status": "INTELLIGENCE_UPDATE",
            "html_size_kb": 156.7,
            "total_time_ms": 892.5,
            "content_hash": "a1b2c3d4e5f67890123456789012345678901234567890123456789012345678"
        },
        {
            "timestamp": "2026-03-16T14:15:00+00:00", 
            "service": {
                "name": "Rockstar Newswire",
                "url": "https://www.rockstargames.com/newswire",
                "keywords": ["Rockstar", "News", "GTA"]
            },
            "status": "INTELLIGENCE_UPDATE",
            "html_size_kb": 89.3,
            "total_time_ms": 645.2,
            "content_hash": "b2c3d4e5f6a17890123456789012345678901234567890123456789012345678"
        },
        {
            "timestamp": "2026-03-17T09:45:00+00:00",
            "service": {
                "name": "PlayStation Store - GTA VI",
                "url": "https://www.playstation.com/en-us/games/grand-theft-auto-vi/",
                "keywords": ["Grand Theft Auto", "GTA VI", "PlayStation"]
            },
            "status": "INTELLIGENCE_UPDATE", 
            "html_size_kb": 234.1,
            "total_time_ms": 1123.7,
            "content_hash": "c3d4e5f6a1b27890123456789012345678901234567890123456789012345678"
        }
    ]
    
    print("Gerando entradas de blog de teste...")
    
    for i, entry in enumerate(test_entries):
        # Converte timestamp para datetime
        timestamp = datetime.datetime.fromisoformat(entry["timestamp"])
        
        # Gera nome do arquivo
        filename = f"update-{timestamp.strftime('%Y-%m-%d-%H-%M')}.html"
        filepath = os.path.join('blog', filename)
        
        # Gera conteúdo HTML do blog
        blog_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intelligence Update - {entry['service']['name']}</title>
    <link rel="stylesheet" href="../assets/style.css">
    <style>
        .blog-post {{
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .post-header {{
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 2rem;
            margin-bottom: 2rem;
        }}
        
        .post-meta {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
            color: var(--text-tertiary);
            font-size: 0.9rem;
        }}
        
        .post-title {{
            color: var(--text-primary);
            margin-bottom: 1rem;
        }}
        
        .status-badge {{
            padding: 0.5rem 1rem;
            border-radius: 4px;
            font-weight: bold;
            text-transform: uppercase;
        }}
        
        .status-secure {{
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }}
        
        .status-warning {{
            background: #fff3cd;
            color: #856404;
            border: 1px solid #ffeaa7;
        }}
        
        .post-content {{
            line-height: 1.6;
            color: var(--text-secondary);
        }}
        
        .metric-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }}
        
        .metric-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            padding: 1.5rem;
            border-radius: 8px;
        }}
        
        .metric-label {{
            color: var(--text-tertiary);
            font-size: 0.8rem;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }}
        
        .metric-value {{
            color: var(--text-primary);
            font-size: 1.2rem;
            font-weight: bold;
        }}
        
        .back-link {{
            margin-top: 2rem;
            display: inline-block;
            padding: 0.5rem 1rem;
            border: 1px solid var(--border-color);
            background: var(--bg-secondary);
            color: var(--text-primary);
            text-decoration: none;
            border-radius: 4px;
            transition: all 0.2s;
        }}
        
        .back-link:hover {{
            background: var(--accent-color);
            color: white;
            border-color: var(--accent-color);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="header-content">
                <div class="logo">
                    <span class="logo-icon">🔍</span>
                    <span class="logo-text">Project Vice Monitor</span>
                </div>
                <nav class="nav">
                    <a href="../index.html" class="nav-link">Dashboard</a>
                    <a href="../blog.html" class="nav-link active">Intelligence Blog</a>
                </nav>
            </div>
        </header>

        <main class="main">
            <div class="blog-post">
                <div class="post-header">
                    <div class="post-meta">
                        <span class="status-badge status-secure">SECURE</span>
                        <span>📅 {timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}</span>
                        <span>🌐 {entry['service']['name']}</span>
                    </div>
                    <h1 class="post-title">Intelligence Update - {timestamp.strftime('%B %d, %Y at %H:%M UTC')}</h1>
                    <p class="post-subtitle">Content change detected on {entry['service']['name']}</p>
                </div>

                <div class="post-content">
                    <h2>Summary</h2>
                    <p>Content change detected on {entry['service']['name']}. The page content has been modified, indicating a potential update or change in the monitored service.</p>

                    <h2>Details</h2>
                    <div class="metric-grid">
                        <div class="metric-card">
                            <div class="metric-label">Detection Time</div>
                            <div class="metric-value">{timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-label">Service Type</div>
                            <div class="metric-value">Website</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-label">Content Size</div>
                            <div class="metric-value">{entry['html_size_kb']} KB</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-label">Response Time</div>
                            <div class="metric-value">{entry['total_time_ms']} ms</div>
                        </div>
                    </div>

                    <h3>Keywords Monitored</h3>
                    <p>{', '.join(entry['service']['keywords'])}</p>

                    <h2>Security Analysis</h2>
                    <p>The change has been flagged as <strong>SECURE</strong> based on the monitoring system's assessment.</p>

                    <h2>Next Steps</h2>
                    <p>Monitor this service for any additional changes or updates that may follow this intelligence update.</p>

                    <div style="margin-top: 2rem; padding: 1rem; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 4px;">
                        <strong>Note:</strong> This entry was automatically generated by the Project Vice Monitor system.
                    </div>
                </div>

                <div style="margin-top: 3rem; display: flex; gap: 1rem;">
                    <a href="../blog.html" class="back-link">← Back to Blog</a>
                    <a href="{entry['service']['url']}" class="back-link" target="_blank">Visit Service →</a>
                </div>
            </div>
        </main>

        <footer class="footer">
            <div class="footer-content">
                <p>&copy; 2026 Project Vice Monitor. Real-time intelligence monitoring system.</p>
            </div>
        </footer>
    </div>
</body>
</html>"""
        
        # Salva arquivo markdown
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(blog_content)
        
        # Gera dados JSON
        json_data = {
            "date": entry["timestamp"],
            "service": entry['service']['name'],
            "url": entry['service']['url'],
            "status": "SECURE",
            "content_size_kb": entry['html_size_kb'],
            "response_time_ms": entry['total_time_ms']
        }
        
        # Salva arquivo JSON
        json_filepath = filepath.replace('.html', '.json')
        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        print(f"Criado: {filename}")
        print(f"JSON: {json_filepath}")
    
    print(f"\nEntradas de blog de teste criadas com sucesso!")
    print("\nArquivos criados:")
    print("- blog/update-2026-03-15-10-30.md")
    print("- blog/update-2026-03-15-10-30.json")
    print("- blog/update-2026-03-16-14-15.md")
    print("- blog/update-2026-03-16-14-15.json")
    print("- blog/update-2026-03-17-09-45.md")
    print("- blog/update-2026-03-17-09-45.json")

def generate_test_history():
    """Gera histórico de testes para simular monitoramento"""
    
    print("\nGerando histórico de testes...")
    
    # Histórico de monitoramento
    test_history = {
        "services": {
            "gta_vi_official": [
                {
                    "timestamp": "2026-03-17T20:00:00+00:00",
                    "url": "https://www.rockstargames.com/VI/",
                    "status": "ONLINE",
                    "http_code": 200,
                    "total_time_ms": 750.2,
                    "dns_time_ms": 12.5,
                    "tcp_time_ms": 156.3,
                    "transfer_time_ms": 581.4,
                    "content_ok": True,
                    "found_keywords": ["Grand Theft Auto", "GTA VI"],
                    "security_headers": {
                        "strict-transport-security": True,
                        "x-content-type-options": True
                    },
                    "content_hash": "abc123def4567890123456789012345678901234567890123456789012345678",
                    "intelligence_update": False,
                    "html_size_kb": 145.6,
                    "num_images": 12,
                    "num_links": 45,
                    "num_scripts": 8,
                    "num_stylesheets": 3,
                    "page_title": "Grand Theft Auto VI",
                    "meta_description": "The official website for Grand Theft Auto VI"
                }
            ],
            "rockstar_newswire": [
                {
                    "timestamp": "2026-03-17T20:00:00+00:00",
                    "url": "https://www.rockstargames.com/newswire",
                    "status": "ONLINE",
                    "http_code": 200,
                    "total_time_ms": 620.8,
                    "dns_time_ms": 8.2,
                    "tcp_time_ms": 134.7,
                    "transfer_time_ms": 477.9,
                    "content_ok": True,
                    "found_keywords": ["Rockstar", "News"],
                    "security_headers": {
                        "strict-transport-security": True,
                        "x-content-type-options": True
                    },
                    "content_hash": "def456abc1237890123456789012345678901234567890123456789012345678",
                    "intelligence_update": False,
                    "html_size_kb": 92.3,
                    "num_images": 8,
                    "num_links": 23,
                    "num_scripts": 5,
                    "num_stylesheets": 2,
                    "page_title": "Rockstar Newswire",
                    "meta_description": "Latest news from Rockstar Games"
                }
            ],
            "playstation_store": [
                {
                    "timestamp": "2026-03-17T20:00:00+00:00",
                    "url": "https://www.playstation.com/en-us/games/grand-theft-auto-vi/",
                    "status": "ONLINE",
                    "http_code": 200,
                    "total_time_ms": 980.5,
                    "dns_time_ms": 15.1,
                    "tcp_time_ms": 189.2,
                    "transfer_time_ms": 776.2,
                    "content_ok": True,
                    "found_keywords": ["Grand Theft Auto", "GTA VI"],
                    "security_headers": {
                        "strict-transport-security": True,
                        "x-content-type-options": True
                    },
                    "content_hash": "ghi789jkl0127890123456789012345678901234567890123456789012345678",
                    "intelligence_update": False,
                    "html_size_kb": 187.4,
                    "num_images": 15,
                    "num_links": 38,
                    "num_scripts": 12,
                    "num_stylesheets": 4,
                    "page_title": "Grand Theft Auto VI | PlayStation Store",
                    "meta_description": "Buy Grand Theft Auto VI at PlayStation Store"
                }
            ],
            "xbox_store": [
                {
                    "timestamp": "2026-03-17T20:00:00+00:00",
                    "url": "https://www.xbox.com/en-US/games/store/grand-theft-auto-vi/9NL3WWNZLZZN",
                    "status": "ONLINE",
                    "http_code": 200,
                    "total_time_ms": 1150.3,
                    "dns_time_ms": 18.7,
                    "tcp_time_ms": 215.4,
                    "transfer_time_ms": 916.2,
                    "content_ok": True,
                    "found_keywords": ["Grand Theft Auto", "GTA VI"],
                    "security_headers": {
                        "strict-transport-security": True,
                        "x-content-type-options": True
                    },
                    "content_hash": "mno345pqr6787890123456789012345678901234567890123456789012345678",
                    "intelligence_update": False,
                    "html_size_kb": 215.8,
                    "num_images": 18,
                    "num_links": 52,
                    "num_scripts": 15,
                    "num_stylesheets": 5,
                    "page_title": "Grand Theft Auto VI | Xbox",
                    "meta_description": "Get Grand Theft Auto VI on Xbox"
                }
            ]
        },
        "created_at": "2026-03-17T19:00:00+00:00",
        "page_size_history": [
            {
                "timestamp": "2026-03-17T19:00:00+00:00",
                "page_size_kb": 145.6,
                "change_percent": 0.0
            }
        ]
    }
    
    # Salva histórico
    with open('history.json', 'w', encoding='utf-8') as f:
        json.dump(test_history, f, indent=2, ensure_ascii=False)
    
    print("Histórico de testes salvo em history.json")
    
    # Gera dados do dashboard
    dashboard_data = {
        "services": {
            "gta_vi_official": {
                "current_status": "ONLINE",
                "sla_24h": 100.0,
                "sla_7d": 100.0,
                "sla_30d": 100.0,
                "performance": {
                    "avg_latency": 750.2,
                    "avg_dns_time": 12.5,
                    "avg_tcp_time": 156.3,
                    "avg_transfer_time": 581.4,
                    "peak_hour": "20:00",
                    "slowest_response": 750.2,
                    "fastest_response": 750.2
                },
                "last_check": "2026-03-17T20:00:00+00:00",
                "engagement": {}
            },
            "rockstar_newswire": {
                "current_status": "ONLINE",
                "sla_24h": 100.0,
                "sla_7d": 100.0,
                "sla_30d": 100.0,
                "performance": {
                    "avg_latency": 620.8,
                    "avg_dns_time": 8.2,
                    "avg_tcp_time": 134.7,
                    "avg_transfer_time": 477.9,
                    "peak_hour": "20:00",
                    "slowest_response": 620.8,
                    "fastest_response": 620.8
                },
                "last_check": "2026-03-17T20:00:00+00:00",
                "engagement": {}
            },
            "playstation_store": {
                "current_status": "ONLINE",
                "sla_24h": 100.0,
                "sla_7d": 100.0,
                "sla_30d": 100.0,
                "performance": {
                    "avg_latency": 980.5,
                    "avg_dns_time": 15.1,
                    "avg_tcp_time": 189.2,
                    "avg_transfer_time": 776.2,
                    "peak_hour": "20:00",
                    "slowest_response": 980.5,
                    "fastest_response": 980.5
                },
                "last_check": "2026-03-17T20:00:00+00:00",
                "engagement": {}
            },
            "xbox_store": {
                "current_status": "ONLINE",
                "sla_24h": 100.0,
                "sla_7d": 100.0,
                "sla_30d": 100.0,
                "performance": {
                    "avg_latency": 1150.3,
                    "avg_dns_time": 18.7,
                    "avg_tcp_time": 215.4,
                    "avg_transfer_time": 916.2,
                    "peak_hour": "20:00",
                    "slowest_response": 1150.3,
                    "fastest_response": 1150.3
                },
                "last_check": "2026-03-17T20:00:00+00:00",
                "engagement": {}
            }
        },
        "incident_log": [],
        "badge": {
            "schemaVersion": 1,
            "label": "Uptime",
            "message": "100.0%",
            "color": "brightgreen"
        },
        "history": test_history["services"],
        "page_size_history": test_history["page_size_history"],
        "generated_at": "2026-03-17T20:00:00+00:00",
        "summary": {
            "run_duration_seconds": 15.2,
            "incidents_last_24h": {
                "gta_vi_official": 0,
                "rockstar_newswire": 0,
                "playstation_store": 0,
                "xbox_store": 0
            },
            "avg_latency_last_24h": {
                "gta_vi_official": 750,
                "rockstar_newswire": 620,
                "playstation_store": 980,
                "xbox_store": 1150
            },
            "intelligence_updates": []
        }
    }
    
    # Salva dados do dashboard
    with open('data/dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    
    print("Dados do dashboard salvos em data/dataset.json")
    
    # Gera badge
    badge_data = {
        "schemaVersion": 1,
        "label": "Uptime",
        "message": "100.0%",
        "color": "brightgreen"
    }
    
    with open('uptime-badge.json', 'w', encoding='utf-8') as f:
        json.dump(badge_data, f, indent=2, ensure_ascii=False)
    
    print("Badge salvo em uptime-badge.json")

def generate_test_chart_history():
    """Gera histórico de gráficos de teste"""
    
    print("\nGerando histórico de gráficos de teste...")
    
    # Histórico de latência (últimas 24 horas)
    chart_history = {
        "latency_labels": [],
        "gta6_latency": [],
        "news_latency": [],
        "ps_latency": [],
        "xbox_latency": []
    }
    
    # Gera dados para últimas 24 horas
    current_time = datetime.datetime.now()
    
    for i in range(24):
        hour_ago = current_time - datetime.timedelta(hours=23-i)
        time_label = hour_ago.strftime('%H:%M')
        
        chart_history["latency_labels"].append(time_label)
        chart_history["gta6_latency"].append(random.randint(600, 900))
        chart_history["news_latency"].append(random.randint(500, 800))
        chart_history["ps_latency"].append(random.randint(800, 1200))
        chart_history["xbox_latency"].append(random.randint(1000, 1500))
    
    # Salva histórico de gráficos
    with open('data/chart_history.json', 'w', encoding='utf-8') as f:
        json.dump(chart_history, f, indent=2, ensure_ascii=False)
    
    print("Histórico de gráficos salvo em data/chart_history.json")

if __name__ == "__main__":
    print("Project Vice Monitor - Gerador de Dados de Teste")
    print("=" * 50)
    
    # Gera entradas de blog
    generate_test_blog_entries()
    
    # Gera histórico de monitoramento
    generate_test_history()
    
    # Gera histórico de gráficos
    generate_test_chart_history()
    
    print("\n" + "=" * 50)
    print("Dados de teste gerados com sucesso!")
    print("\nPróximos passos:")
    print("1. Execute: python -m http.server 8000")
    print("2. Acesse: http://localhost:8000")
    print("3. Verifique o dashboard e o blog")
    print("\nArquivos criados:")
    print("- blog/update-*.md (entradas de blog)")
    print("- blog/update-*.json (dados estruturados)")
    print("- history.json (histórico de monitoramento)")
    print("- data/dataset.json (dados do dashboard)")
    print("- data/chart_history.json (histórico de gráficos)")
    print("- uptime-badge.json (badge de status)")