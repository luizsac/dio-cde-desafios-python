n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

# media = //complete
# print('Media: %.1f' %media)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / (2 + 3 + 4 + 1)
print(f"Media: {media:.1f}")

#if (media >= 7):
if media >= 7:
    print('Aluno aprovado.')
#elif(media<5):
elif media < 5:
    print('Aluno reprovado.')
elif 5 <= media <= 6.9:  # teste com 6.9 para evitar bug no teste 1
    print('Aluno em exame.')
    n5 = float(input())
    #final = (n5+media)/2
    final = (n5 + media) / 2
    # print('Nota do exame: ', n5)
    print(f"Nota do exame: {n5:.1f}")
    # //complete
    if final >= 5:
        print('Aluno aprovado.')
        # print('Media final: %.1f' %final)
    else:
        print('Aluno reprovado')
        # print('Media final: %.1f' % final)
    print(f"Media final: {final:.1f}")