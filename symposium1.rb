require 'rubygems'
require 'selenium-webdriver'

driver = Selenium::WebDriver.for :chrome, :switches => %w[--ignore-certificate-errors --disable-popup-blocking --disable-translate]
driver.get "http://collaborative.ase.ro/files/Default.aspx"

element = driver.find_element :id => "DropDownList1"
element.send_keys "Dr."

element = driver.find_element :id => "tb_first_name"
element.send_keys "Cristian"

element = driver.find_element :id => "tb_last_name"
element.send_keys "CIUREA"

element = driver.find_element :id => "DropDownList5"
element.send_keys "Assistant professor"

element = driver.find_element :id => "DropDownList6"
element.send_keys "Economic informatics"

element = driver.find_element :id => "tb_address"
element.send_keys "Bucharest"

element = driver.find_element :id => "tb_street"
element.send_keys "Calea Dorobantilor"

element = driver.find_element :id => "tb_number"
element.send_keys "1517"

element = driver.find_element :id => "tb_city"
element.send_keys "Bucharest"

element = driver.find_element :id => "tb_state"
element.send_keys "Bucharest"

element = driver.find_element :id => "tb_zip"
element.send_keys "010552"

element = driver.find_element :id => "DropDownList7"
element.send_keys "Romania"

element = driver.find_element :id => "tb_phone"
element.send_keys "0213191900"

element = driver.find_element :id => "tb_email"
element.send_keys "cristianciurea@ase.ro"

element = driver.find_element :id => "tb_fax"
element.send_keys "0213191991"

element = driver.find_element :id => "DropDownList2"
element.send_keys "No"

element = driver.find_element :id => "DropDownList3"
element.send_keys "Students - 100 euro"

element = driver.find_element :id => "DropDownList4"
element.send_keys "Visa"

element = driver.find_element :id => "tb_card_number"
element.send_keys "1234567890123456"

element = driver.find_element :id => "tb_expiration"
element.send_keys "1226"

element = driver.find_element :id => "tb_comments"
element.send_keys "No comments"

sleep 5
element = driver.find_element :id => "Button1"
element.click

wait = Selenium::WebDriver::Wait.new(:timeout => 5)
puts "Test Passed: Form successfully completed!" if wait.until {
	element = driver.find_element :id => "Label1"
	element if element.displayed?
}

sleep 5

puts "Test Passed!" if wait.until {
    /Your registration was successfully completed!/.match(driver.page_source)
}

sleep 5
driver.quit
