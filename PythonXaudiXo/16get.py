contacts = {
  'Ivan Petrov' : '1234',
  'Bugalteria' : {
    'Svitlana Jank' : '5415',
    'luba Proc' : '6515',
    'Bogdan Kuk' : '445',
    },
  'Valia Vorobej' : '5616',
  'Slavik Kaj' : '145',
  'Oleg Li' : '66165',
  '111' : 5565
}
testing = input('Кого шукаєте?: ')

if testing in contacts:
  print( contacts.get(testing, 'Номер не знайдено') )

else:
  print('Контакт не знайдено!')



