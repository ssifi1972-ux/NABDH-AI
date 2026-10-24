class DigitalFoodSafetyConsortium:
    def __init__(self):
        """
        منظومة نَبْضْ ومرجان المدمجة للأمن البيولوجي القومي
        المراجع: وزارة الفلاحة الجزائرية (حظر ذبح الإناث) | Codex Alimentarius | FAO | WHO
        """
        self.SAFE_MEAT_PH_MAX = 5.8
        self.MAX_SAFE_HISTAMINE_PPM = 100 

    def verify_red_meat_and_organs(self, animal_type, progesterone_level, ph_level, is_organ=False):
        """
        [منظومة نَبْضْ] - تفكيك الهيكل البيولوجي للحوم الحمراء والأحشاء
        """
        # كشف وفيات المسالخ العشوائية ولحوم الخنق والصعق
        if ph_level > self.SAFE_MEAT_PH_MAX:
            return {
                "status": "🔴 خطر أحمر (لحم تالف/ميتة)",
                "cause": "احتباس دموي بكتيري حاد نتيجة الموت بالخنق أو الصعق الكهربائي القاتل.",
                "action": "حظر الختم الرقمي آلياً، ومصادرة الشحنة، وتبليغ مصالح قمع الغش فوراً."
            }
        
        # كشف ذبح إناث الماشية الحوامل (النعاج/الأبقار العِشار) بعد السلخ هرمونياً
        if progesterone_level > 65.0:
            return {
                "status": "🔴 خطر أحمر (إهدار الأجنة وغش بيولوجي)",
                "cause": f"النسيج العضلي المعلق يعود لأنثى حامل سقط جنينها سراً (مستوى البروجسترون: {progesterone_level} نانوجرام).",
                "action": "تجميد المعاملة التجارية، الحصانة القانونية للبيطري، وإرسال تقرير مشفر لمديرية المصالح الفلاحية."
            }
            
        return {
            "status": "🟢 آمن وحلال", 
            "cause": "مستنزف الدم تماماً، مطابق للتذكية الشرعية والمعايير البيطرية.", 
            "action": "توليد رمز البصمة الرقمية (NABDH QR)."
        }

    def verify_seafood_and_poultry(self, product_type, histamine_ppm, formalin_detected, poultry_dead_on_arrival=False):
        """
        [منظومة مَرْجَانْ ودواجن اللاحم] - كشف ميتة الدجاج والسمك الفاسد الموجه للفرم والمصبرات
        """
        # كشف غش الدجاج الميت جراء النقل الموجه لفرم الكاشير والمرتديلا والمطاعم
        if product_type == "poultry" and poultry_dead_on_arrival:
            return {
                "status": "🔴 خطر أحمر (دجاج ميت/وفيات شاحنات النقل)",
                "cause": "فرم سري لـ دواجن ميتة ومخنوقة تم خلطها بالتوابل والمضافات الكيميائية لإخفاء الفساد.",
                "action": "إتلاف الشحنة فوراً، حظر منتجات المصنع، وإدراج العلامة التجارية في القائمة السوداء للتسممات."
            }
            
        # كشف الغش الكيميائي المسرطن في الأسماك (الفورمول) والتسمم الهستاميني المقاوم للطهي
        if product_type == "fish":
            if formalin_detected:
                return {
                    "status": "🔴 خطر أحمر (مسرطنات حادة)", 
                    "cause": "غسل الأسماك بمادة الفورمول المحظورة لإعطائها قواماً متماسكاً كاذباً.", 
                    "action": "غلق المحل قضائياً ومصادرة الأسماك السامة."
                }
            if histamine_ppm > self.MAX_SAFE_HISTAMINE_PPM:
                return {
                    "status": "🔴 خطر أحمر (تسمم هستاميني فتاك)", 
                    "cause": f"ارتفاع غاز الهستامين لـ {histamine_ppm} ppm بسبب كسر التبريد وهو مقاوم للطهي والمصبرات.", 
                    "action": "منع الشحنة من التداول لخطر الوفاة الفورية للمستهلك."
                }
                
        return {
            "status": "🟢 آمن وطازج ومطابق", 
            "cause": "خالٍ من الملوثات الكيميائية ومطابق لمعايير الاستدامة والصحة.", 
            "action": "توليد رمز الأمان الرقمي (MARJAN QR)."
        }

# --- تشغيل المحاكاة الفورية في الـ Terminal ---
if __name__ == "__main__":
    consortium = DigitalFoodSafetyConsortium()
    print("="*65)
    print(" تشغيل البيئة التجريبية المدمجة لمنظومتي [نَبْضْ AI] و [مَرْجَانْ AI] ")
    print("="*65)
    
    # محاكاة حالة غياب البيطري والعثور على لحم بقرة معلق مسلوخ
    print("\n[المسلخ البلدي]: فحص نسيج اللحوم الحمراء المعلقة بعد السلخ...")
    test_1 = consortium.verify_red_meat_and_organs(animal_type="cow", progesterone_level=82.0, ph_level=5.5)
    print(f"النتيجة: {test_1['status']}\nالسبب الميداني: {test_1['cause']}\nالإجراء القانوني: {test_1['action']}")
    print("-" * 65)
    
    # محاكاة فحص شحنة سردين قادمة من ميناء الصيد
    print("\n[ميناء الصيد / سوق الجملة]: فحص شحنة أسماك سطحية (سردين)...")
    test_2 = consortium.verify_seafood_and_poultry(product_type="fish", histamine_ppm=145, formalin_detected=False)
    print(f"النتيجة: {test_2['status']}\nالسبب الميداني: {test_2['cause']}\nالإجراء القانوني: {test_2['action']}")
    print("="*65)
