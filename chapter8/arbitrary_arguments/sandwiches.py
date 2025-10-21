def sandwiches(*indhold):
    print(f'Her er din sandwich med følgende:')
    for indhold in indhold:
        print(f'- {indhold.title()}')

sandwiches('tomat', 'ost', 'chorizo', 'parma skinke')