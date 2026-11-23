#!/usr/bin/env python3
"""Offline repository checks; does not claim model behavior, legal compliance or remote CI success."""
from __future__ import annotations

import importlib.util
import json
import re
import struct
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "SKILL.md", "SKILL.en.md", "README.md", "README.en.md", "LICENSE",
    "CHANGELOG.md", "ROADMAP.md", "CONTRIBUTING.md", "agents/openai.yaml",
    "examples/README.md", "examples/durian-worked-example.md",
    "references/compliance-rules.md", "references/platform-playbooks.md",
    "references/output-contracts.md", "references/source-notes.md",
    "references/copy-quality-rules.md", "references/category-notes.md", "scripts/scan-final-copy.py",
    "assets/showcase-output.svg", "test-prompts.json",
    ".claude-plugin/marketplace.json", ".claude-plugin/plugin.json",
    ".github/workflows/verify.yml", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.md", ".github/ISSUE_TEMPLATE/rule_update.md",
    ".github/ISSUE_TEMPLATE/example_request.md",
    "tools/evaluate-prompts.py", "tools/package-skill.py", "scripts/count-copy.py", "tests/test_validation.py",
]
CHECKS = {
    "SKILL.md": ["sổ bằng chứng", "Chế độ giao một lần", "Reference Fidelity", "Negative Prompt",
                 "Giá/combo/khuyến mãi", "Mặc định chế độ", "Quy cách chữ trên ảnh", "Cách render chữ", "Tự kiểm quy cách chữ",
                 "Quá tải chữ", "hậu kỳ", "references/output-contracts.md", "Pass/Fail năm chiều", "quy tắc thực thi Luật Quảng cáo", "Tự kiểm tuân thủ quảng cáo Việt Nam",
                 "Bảng hỏi khởi động", "Trang danh sách, màn hình đầu và ảnh bìa", "Ba cửa cho hỏi–đáp", "Biên bản tự chấm", "80 điểm", "Tự chấm đạt mới giao", "Tự kiểm chất lượng nội dung", "tự đủ nghĩa", "references/copy-quality-rules.md", "references/category-notes.md", "Tự kiểm KV1 nhận diện", "Xác nhận tên sản phẩm trước khi bắt đầu", "đặt tên theo ảnh"],
    "SKILL.en.md": ["Evidence ledger", "One-shot", "Reference Fidelity",
                    "Negative Constraints", "Price / bundle / promotion", "Default mode", "Copy specifications",
                    "Text rendering method", "Copy-spec self-check", "Copy overload", "post-production", "Pass/Fail", "Vietnam main-image", "Vietnam advertising compliance check",
                    "Kickoff questionnaire", "Listing pages, first screens and covers", "Question checks", "Self-review record", "80-point", "Deliver only after the self-review passes", "Copy quality self-check", "self-contained", "references/copy-quality-rules.md", "references/category-notes.md", "KV1 recognition check", "Confirm the product name at the start", "image-based proposed name"],
    "README.md": ["npx skills add feichanggege/ecommerce-visual-copywriting-skill",
                  "Sổ bằng chứng", "Playbook đa nền tảng", "assets/showcase-output.svg", "Ranh giới an toàn"],
    "README.en.md": ["Quick Start", "Evidence Ledger", "Reference Fidelity", "Platforms", "Safety"],
    "agents/openai.yaml": ["display_name:", "short_description:"],
    "references/platform-playbooks.md": ["Amazon", "Shopify", "TikTok Shop", "Shopee Việt Nam",
                                         "Lazada Việt Nam", "Tiki / Sendo", "Facebook / Instagram / Zalo", "Temu"],
    "references/compliance-rules.md": ["Trạng thái bằng chứng", "Thực phẩm thông thường/đồ uống", "Tính cập nhật của quy định nền tảng", "Danh mục nguồn", "source-notes.md", "VN-AD-ND", "Thực thi nội dung ảnh chính/ảnh chi tiết tại Việt Nam"],
    "references/output-contracts.md": ["Sổ bằng chứng", "Storyboard", "Báo cáo kiểm tra/sửa bản", "Bàn giao bản địa hóa xuyên biên giới",
                                       "Cách render chữ", "Tự kiểm quy cách chữ", "Tự kiểm tuân thủ quảng cáo Việt Nam", "Lớp chữ cuối cùng", "Biên bản tự chấm", "Tự kiểm KV1 nhận diện", "Tên sản phẩm gốc", "nguồn đặt tên"],
}
SECTION_PAIRS = [
    ("Nguyên tắc vận hành", "Core principles"),
    ("Chế độ thực thi", "Execution modes"),
    ("Bước 0: Định tuyến nhiệm vụ và đầu vào tối thiểu", "Step 0 — Task routing and minimum inputs"),
    ("Bước 1: Lập sổ bằng chứng", "Step 1 — Build an evidence ledger"),
    ("Bước 2: Xác định động lực chốt đơn", "Step 2 — Select the conversion driver"),
    ("Bước 3: Khóa Campaign Style Lock", "Step 3 — Lock the Campaign Style"),
    ("Bước 4: Lên Storyboard", "Step 4 — Plan the storyboard"),
    ("Bước 5: Xuất bản thực thi", "Step 5 — Execute"),
    ("Chữ trên ảnh và cách render chữ", "On-image copy and text rendering"),
    ("Bước 6: Cổng chất lượng năm chiều", "Step 6 — Five-part quality gate"),
    ("Tuân thủ và tính cập nhật", "Compliance and currency"),
    ("Quy tắc nạp tài liệu tham chiếu", "Reference loading"),
    ("Các lỗi thường gặp then chốt", "Key failure modes"),
]
EXPECTED_CASES = {
    "standard_storyboard_gate", "amazon_one_shot_localization", "ordinary_food_claim_boundary",
    "audit_minimum_change", "reference_fidelity_lock", "shopify_cross_border_localization",
    "minimal_information", "competitor_comparison", "baby_product_boundary",
    "health_food_approved_scope", "promotion_conditions", "explicit_model_text",
    "designer_handoff_pdp", "one_shot_single_reason",
    "vn_absolute_claim_rewrite", "vn_medical_wordplay", "vn_cited_test_scope",
    "vn_visible_promotion_terms", "vn_regulated_ad_approval", "vn_usage_not_superlative",
    "kv1_original_skirt_necklace", "kv1_original_tassel_necklace", "kv1_no_added_text",
    "kv2_feature_headline", "kv1_rack_recognition",
    "name_missing_at_start", "authorized_visual_naming",
    "kickoff_questionnaire", "kickoff_skip", "self_review_gate", "unproven_claim_not_placeholder",
}
SECRET_PATTERNS = [
    re.compile(r"gh[op]_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"""(?i)(api[_-]?key|token|cookie|secret|password)\s*[:=]\s*['"]?[^'"\s]{8,}"""),
    re.compile(r"[A-Z]:\\Users\\[^\\\s]+"),
]
TEXT_SUFFIXES = {".md", ".json", ".py", ".svg", ".txt", ".yml", ".yaml"}


def require_text(label: str, text: str, needles: list[str]) -> None:
    for needle in needles:
        if needle.casefold() not in text.casefold():
            raise ValueError(f"{label} missing expected text: {needle}")


def check_frontmatter(text: str) -> None:
    parts = text.split("---\n", 2)
    if not text.startswith("---\n") or len(parts) != 3:
        raise ValueError("SKILL.md must start with closed YAML frontmatter")
    header = parts[1]
    keys = set(re.findall(r"^([A-Za-z0-9_-]+):", header, re.MULTILINE))
    if keys != {"name", "description"}:
        raise ValueError("SKILL.md frontmatter keys must be name and description")
    if not re.search(r"^name:\s*ecommerce-visual-copywriting\s*$", header, re.MULTILINE):
        raise ValueError("SKILL.md name is invalid")
    description = re.search(r"^description:\s*(.+)$", header, re.MULTILINE)
    if not description or not 80 <= len(description.group(1).strip()) <= 1024:
        raise ValueError("SKILL.md description length must be 80–1024 characters")
    if len(text.splitlines()) > 500:
        raise ValueError("SKILL.md exceeds the 500-line progressive-loading target")


def check_bilingual_sections(chinese: str, english: str) -> None:
    for index, (text, label) in enumerate(((chinese, "SKILL.md"), (english, "SKILL.en.md"))):
        headings = re.findall(r"^## (.+)$", text, re.MULTILINE)
        expected = [pair[index] for pair in SECTION_PAIRS]
        if [h.casefold() for h in headings] != [h.casefold() for h in expected]:
            raise ValueError(f"{label} top-level sections differ from the bilingual contract")


def check_local_links(root: Path, file: Path, text: str) -> None:
    targets = re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)|(?:src|href)="([^"]+)"', text)
    for markdown, html in targets:
        target = markdown or html
        if markdown:
            target = re.sub(r'''\s+(?:"[^"]*"|'[^']*')$''', "", target)
        target = target.strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        path = (file.parent / unquote(parsed.path)).resolve()
        if not path.is_relative_to(root.resolve()) or not path.exists():
            raise ValueError(f"broken local file link in {file.relative_to(root)}: {target}")


def jpeg_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:2] != b"\xff\xd8":
        raise ValueError(f"invalid JPEG: {path.name}")
    offset = 2
    while offset + 4 <= len(data):
        if data[offset] != 0xFF:
            raise ValueError(f"invalid JPEG marker: {path.name}")
        marker = data[offset + 1]
        offset += 2
        length = struct.unpack(">H", data[offset:offset + 2])[0]
        if marker in {0xC0, 0xC1, 0xC2}:
            height, width = struct.unpack(">HH", data[offset + 3:offset + 7])
            return width, height
        if length < 2:
            break
        offset += length
    raise ValueError(f"JPEG dimensions missing: {path.name}")


def check_assets(root: Path, docs: str) -> None:
    for asset in (root / "assets").rglob("*"):
        if not asset.is_file():
            continue
        if asset.stat().st_size > 500_000:
            raise ValueError(f"asset exceeds 500,000 bytes: {asset.relative_to(root)}")
        if asset.relative_to(root).as_posix() not in docs:
            raise ValueError(f"unreferenced public asset: {asset.relative_to(root)}")
    original = root / "assets/showcase/sau-rieng-ri6-main.jpg"
    thumb = root / "assets/showcase/thumbs/sau-rieng-ri6-main-thumb.jpg"
    width, height = jpeg_size(original)
    twidth, theight = jpeg_size(thumb)
    if abs(width / height - twidth / theight) > 0.002:
        raise ValueError("durian thumbnail must preserve the complete source aspect ratio")
    ElementTree.parse(root / "assets/showcase-output.svg")


def check_plugin(root: Path) -> None:
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    manifest = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if marketplace["name"] != "ecommerce-visual-copywriting-skill":
        raise ValueError("marketplace name differs from installation instructions")
    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1 or plugins[0].get("source") != "./":
        raise ValueError("marketplace must reference this root skill plugin")
    for key in ("name", "version"):
        if plugins[0].get(key) != manifest.get(key):
            raise ValueError(f"plugin/marketplace {key} mismatch")
    if manifest.get("name") != "ecommerce-visual-copywriting":
        raise ValueError("plugin name differs from installation instructions")


def verify(root: Path = ROOT) -> None:
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            raise ValueError(f"missing required file: {relative}")
    chinese = (root / "SKILL.md").read_text(encoding="utf-8")
    english = (root / "SKILL.en.md").read_text(encoding="utf-8")
    check_frontmatter(chinese)
    check_bilingual_sections(chinese, english)
    for relative, needles in CHECKS.items():
        require_text(relative, (root / relative).read_text(encoding="utf-8"), needles)
    spec = importlib.util.spec_from_file_location("prompt_evaluator", root / "tools/evaluate-prompts.py")
    evaluator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(evaluator)
    cases = evaluator.validate_cases(json.loads((root / "test-prompts.json").read_text(encoding="utf-8")))
    if not EXPECTED_CASES.issubset({case["name"] for case in cases}):
        raise ValueError("test-prompts.json is missing required behavioral coverage")
    check_plugin(root)
    docs = []
    for file in root.rglob("*"):
        relative = file.relative_to(root)
        if any(part in {".git", "__pycache__", "dist"} for part in relative.parts):
            continue
        if not file.is_file() or file.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = file.read_text(encoding="utf-8")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                raise ValueError(f"possible secret or private path in {relative}")
        if file.suffix.lower() in {".md", ".svg"}:
            check_local_links(root, file, text)
        if file.suffix.lower() == ".md" and "archive" not in relative.parts:
            docs.append(text)
    check_assets(root, "\n".join(docs))


def main() -> int:
    try:
        verify()
    except (OSError, ValueError, KeyError, struct.error, ElementTree.ParseError) as exc:
        print(f"FAIL: {exc}")
        return 1
    print("PASS: v3 repository checks passed (structure, bilingual sections, links, assets, prompt schema, privacy)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
