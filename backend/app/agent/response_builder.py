class ResponseBuilder:
    @staticmethod
    def build_fallback_response(intent, tool_results, query_text, lang="te"):
        is_te = lang == "te"

        # 1. Greeting
        if intent == "greeting":
            if is_te:
                return (
                    "నమస్కారం! నేను గ్రామమిత్ర AI (GramaMitra AI) డిజిటల్ సహాయకుడిని. "
                    "కొనంకి గ్రామం మరియు గ్రామీణ ప్రజల కోసం ప్రభుత్వం అమలు చేస్తున్న సంక్షేమ పథకాలు, "
                    "అర్హతలు, అవసరమైన పత్రాలు, మరియు ఇంటర్నెట్ సేవల వివరాలను సులభంగా తెలుసుకోవడానికి నేను మీకు సహాయం చేస్తాను. "
                    "మీరు ఏ పథకం గురించి తెలుసుకోవాలనుకుంటున్నారు?"
                )
            else:
                return (
                    "Namaste! I am GramaMitra AI, your digital literacy and e-governance assistant. "
                    "I help rural citizens understand government welfare schemes, eligibility rules, "
                    "required documents, and digital portals. How may I assist you today?"
                )

        # 2. Portal Error
        if intent == "portal_error" and "portal_error" in tool_results:
            err = tool_results["portal_error"]
            if is_te:
                lines = [
                    f"### ⚠️ సమస్య వివరణ: {err.get('title', 'వెబ్‌సైట్ ఎర్రర్')}",
                    f"{err.get('explanation', '')}\n",
                    "**పరిష్కార చర్యలు (సురక్షితమైన మార్గాలు):**"
                ]
                for idx, step in enumerate(err.get("steps", []), 1):
                    lines.append(f"{idx}. {step}")
                if err.get("warning"):
                    lines.append(f"\n🛡️ **భద్రతా హెచ్చరిక:** {err.get('warning')}")
                return "\n".join(lines)
            else:
                lines = [
                    f"### ⚠️ Issue Diagnosis: {err.get('title', 'Website Error')}",
                    f"{err.get('explanation', '')}\n",
                    "**Recommended Safe Troubleshooting Steps:**"
                ]
                for idx, step in enumerate(err.get("steps", []), 1):
                    lines.append(f"{idx}. {step}")
                if err.get("warning"):
                    lines.append(f"\n🛡️ **Security Warning:** {err.get('warning')}")
                return "\n".join(lines)

        # 3. Documents
        if "documents" in tool_results and tool_results["documents"].get("found"):
            doc_data = tool_results["documents"]
            scheme_name = doc_data.get("scheme_name", "")
            docs = doc_data.get("documents", [])
            if is_te:
                lines = [f"### 📄 {scheme_name} పథకానికి అవసరమైన పత్రాలు:"]
                for d in docs:
                    req_mark = "(తప్పనిసరి)" if d.get("is_mandatory") else "(ఐచ్ఛికం)"
                    lines.append(f"- **{d['document_name']}** {req_mark}: {d['purpose']} (జారీ చేసే వారు: {d['issuing_authority']})")
                lines.append("\n💡 **సలహా:** దరఖాస్తు చేయడానికి వెళ్లే ముందు మీ గ్రామ సచివాలయంలో అన్ని కాపీలను సిద్ధంగా ఉంచుకోండి.")
                return "\n".join(lines)
            else:
                lines = [f"### 📄 Required Documents for {scheme_name}:"]
                for d in docs:
                    req_mark = "(Mandatory)" if d.get("is_mandatory") else "(Optional)"
                    lines.append(f"- **{d['document_name']}** {req_mark}: {d['purpose']} (Issuing Authority: {d['issuing_authority']})")
                lines.append("\n💡 **Tip:** Keep xerox copies and original certificates ready before visiting the Grama Sachivalayam.")
                return "\n".join(lines)

        # 4. Eligibility
        if "eligibility" in tool_results and tool_results["eligibility"].get("found"):
            el_data = tool_results["eligibility"]
            scheme_name = el_data.get("scheme_name", "")
            crit = el_data.get("criteria", [])
            if is_te:
                lines = [f"### 📋 {scheme_name} అర్హత నిబంధనలు:"]
                for c in crit:
                    lines.append(f"- **{c['question']}**: {c['explanation']}")
                lines.append("\n🔍 మీరు పూర్తి అర్హతను ఆన్‌లైన్‌లో పరీక్షించడానికి మా 'అర్హత తనిఖీ' (Eligibility Checker) పేజీని ఉపయోగించవచ్చు.")
                return "\n".join(lines)
            else:
                lines = [f"### 📋 Eligibility Rules for {scheme_name}:"]
                for c in crit:
                    lines.append(f"- **{c['question']}**: {c['explanation']}")
                lines.append("\n🔍 You can test your eligibility interactively using our 'Eligibility Checker' module.")
                return "\n".join(lines)

        # 5. Application Steps
        if "application" in tool_results and tool_results["application"].get("found"):
            app_data = tool_results["application"]
            scheme_name = app_data.get("scheme_name", "")
            steps = app_data.get("steps", [])
            if is_te:
                lines = [f"### 📝 {scheme_name} పథకానికి దరఖాస్తు చేసుకునే విధానం:"]
                for s in steps:
                    lines.append(f"**దశ {s['step_number']}: {s['title']}** ({s['channel']})")
                    lines.append(f"  {s['description']}")
                    if s.get("caution_warning"):
                        lines.append(f"  *గమనిక:* {s['caution_warning']}")
                lines.append(f"\n🌐 అధికారిక పోర్టల్: {app_data.get('official_url', '')}")
                return "\n".join(lines)
            else:
                lines = [f"### 📝 Step-by-Step Application Guide for {scheme_name}:"]
                for s in steps:
                    lines.append(f"**Step {s['step_number']}: {s['title']}** ({s['channel']})")
                    lines.append(f"  {s['description']}")
                    if s.get("caution_warning"):
                        lines.append(f"  *Caution:* {s['caution_warning']}")
                lines.append(f"\n🌐 Official Portal: {app_data.get('official_url', '')}")
                return "\n".join(lines)

        # 6. Scheme Discovery or List
        if "schemes" in tool_results and tool_results["schemes"].get("found"):
            schemes = tool_results["schemes"].get("schemes", [])
            if is_te:
                lines = ["### 🏛️ అందుబాటులో ఉన్న సంక్షేమ పథకాలు:"]
                for s in schemes:
                    lines.append(f"\n**{s['name']}** ({s['state_or_central']})")
                    lines.append(f"- **లబ్ధిదారులు:** {s['target_beneficiaries']}")
                    lines.append(f"- **ప్రయోజనం:** {s['benefits_summary']}")
                    lines.append(f"- **అధికారిక లింక్:** {s['official_url']}")
                lines.append("\nపథకం పూర్తి వివరాలు, అర్హతలు లేదా అవసరమైన డాక్యుమెంట్ల కోసం ఆ పథకం పేరును అడగండి.")
                return "\n".join(lines)
            else:
                lines = ["### 🏛️ Available Government Welfare Schemes:"]
                for s in schemes:
                    lines.append(f"\n**{s['name']}** ({s['state_or_central']})")
                    lines.append(f"- **Beneficiaries:** {s['target_beneficiaries']}")
                    lines.append(f"- **Benefits:** {s['benefits_summary']}")
                    lines.append(f"- **Official Portal:** {s['official_url']}")
                lines.append("\nAsk for any specific scheme name to check its eligibility rules or required documents.")
                return "\n".join(lines)

        # 7. FAQs
        if "faqs" in tool_results and tool_results["faqs"].get("count", 0) > 0:
            faqs = tool_results["faqs"].get("faqs", [])
            lines = ["### 💡 సంబంధిత ప్రశ్నలు & సమాధానాలు:" if is_te else "### 💡 Relevant Questions & Answers:"]
            for f in faqs[:3]:
                lines.append(f"\n**ప్ర: {f['question']}**\nజ: {f['answer']}")
            return "\n".join(lines)

        # 8. Digital Literacy
        if "lessons" in tool_results and tool_results["lessons"].get("count", 0) > 0:
            lessons = tool_results["lessons"].get("lessons", [])
            lines = ["### 📱 డిజిటల్ అక్షరాస్యత పాఠాలు:" if is_te else "### 📱 Digital Literacy Lessons:"]
            for l in lessons:
                lines.append(f"- **{l['title']}** ({l['module_category']}): {l['summary']}")
            lines.append("\nమా 'డిజిటల్ నైపుణ్యాలు' (Learn Digital) విభాగంలో పూర్తి పాఠాలను చదవవచ్చు మరియు క్విజ్ రాయవచ్చు.")
            return "\n".join(lines)

        # Ultimate fallback
        if is_te:
            return (
                "మీరు అడిగిన విషయానికి సంబంధించి సరిపోయే రికార్డు మా వద్ద ప్రస్తుతం లభించలేదు. "
                "దయచేసి పథకం పేరు స్పష్టంగా పేర్కొనండి (ఉదాహరణకు: 'పీఎం కిసాన్', 'పెన్షన్ కానుక', 'తల్లికి వందనం') "
                "లేదా కొనంకి గ్రామ సచివాలయాన్ని సంప్రదించండి."
            )
        else:
            return (
                "We could not find an exact match for your query in the verified database. "
                "Please specify a scheme name (e.g. 'PM-KISAN', 'NTR Bharosa Pension', 'Thalliki Vandanam') "
                "or visit your local Grama Sachivalayam for in-person support."
            )
