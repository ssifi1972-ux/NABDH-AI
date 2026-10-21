# 🐉 CHIMERA Engine - Consensus is Security
from chimera import HEADS
from random import randint

def simulate_attack():
    print("\n🚨 Simulating Malicious Transaction...")
    verdicts = []
    for head in HEADS[2:7]:  # الـ 5 رؤوس الصيادة
        threat = randint(0,1)
        verdicts.append((head.mythic_name, "THREAT" if threat else "SAFE"))
        print(f"  {head.mythic_name}: {'🔴 THREAT' if threat else '🟢 SAFE'}")
    
    # CONCORD يحكم - No Single Head Rules
    threats = sum(1 for _, v in verdicts if v=="THREAT")
    final = "BLOCKED 🔒" if threats >= 3 else "ALLOWED ✅"
    print(f"\n[CONCORD] {threats}/5 heads detected threat -> {final}")
    print(f"[CHRONOS] Human approval required for {final}")

if __name__ == "__main__":
    simulate_attack()