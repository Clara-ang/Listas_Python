def determinar_vencedor(charrete1, charrete2):
    num1, dist1, vel1 = charrete1
    num2, dist2, vel2 = charrete2
  
    vel1_m_s = vel1 / 3.6
    vel2_m_s = vel2 / 3.6

    tempo1 = dist1 / vel1_m_s
    tempo2 = dist2 / vel2_m_s
    
    if tempo1 < tempo2:
        return num1
    else:
        return num2

charrete1 = list(map(int, input().split()))
charrete2 = list(map(int, input().split()))
vencedor = determinar_vencedor(charrete1, charrete2)
print(vencedor)