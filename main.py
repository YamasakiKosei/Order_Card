import ui
import clipboard
import console
import  sound
import collections
import threading
import time



###課題###

#↑を押したメニューの1ページ目の1番下にいく
#これ、難しい
#x.appendする
#len(x)が6で2ページ目の1番目

#2ページ目の1個目のメニューを0にして、↑↓すると1ページ目が出るようにする
#table1.itemsが0になったら、storageから呼び出す

#クリア後、何もないとこでのクリア 例外処理

#担当の途中で上下キーでバグ







#変数を変えるっていうのは難しい
#リストに追加、削除はできる

#カーソルの判別
x = []

#クリアー、0の判別
y = []

#画面切り替えの判別
z = []

#個数
counter = []
#個数表示（1個多くいる）（5番目が1番目にくるから）
counter_disp = ['','','','','']
#個数表示保管
counter_disp_storage = []
#表示される順番
menu_place = []
menu_place_storage = []







# 数字キーのイベント処理
def onBtnTap(sender):
	sound.play_effect('game:Beep')
	global counter
	
		
			
	#担当label
	#リストzになにか入っていたら
	if len(z) > 0:
		if chargelabel.text == '_____':
			chargelabel.text = ''
			#3桁以上は表示しない
		if  len(chargelabel.text) < 2:
			s = chargelabel.text
			chargelabel.text = s + sender.title
		
			
	
	#disp1
	#リストxになにも入ってないなら
	elif  len(x) == 0:
		if disp1.text == '_____':
			disp1.text = ''
			#3桁以上は表示しない
		if  len(disp1.text) < 2:
			s = disp1.text
			disp1.text = s + sender.title
			#卓番があっていないと✗
			if len(disp1.text) == 2:
				table_number = ['01','02','03','04','05','06','07','08','09','10','11','12','13','21','22','23','24','25','26','27','31','32','33','34','35','36','37','38']
				if  not disp1.text in table_number:
					sound.play_effect('game:Error')
					disp1.text = '_____'
				
#送信時の卓番エラーもチェックしよう後で
#1桁がOKになってる

						
		
	#disp2				
	elif  len(x) == 1:
		if disp2.text == '？':
			disp2.text = ''
		t = disp2.text
		#01…とならないようにする
		if t == '0':
			t = ''
		#4桁以上は表示しない
		if len(disp2.text) < 4:
			disp2.text = t + sender.title
	
			
				
	#tableview1[0]
	elif  len(x) == 2:
		NmbBtn(sender,0)	
	#tableview1[1]
	elif  len(x) == 3:
		NmbBtn(sender,1)
	#tableview1[2]
	elif  len(x) == 4:
		NmbBtn(sender,2)
	#tableview1[3]	
	elif  len(x) == 5:
		NmbBtn(sender,3)

		
def NmbBtn(sender,self):
	global counter
	#0ボタンを押されたら
	if sender.title == '0':
		table1.data_source.items[self] = menu_place[self]
		counter_disp[self] = sender.title
		#個数も0にする
		counter = [c for c in counter if c != menu_place[self]]
		#個数0のやつができた証拠
		y.append('y')

	#0以外のボタンを押されたら	
	else:
		table1.data_source.items[self] = menu_place[self]
		counter_disp[self] = sender.title		
		#ボタンの数 > カウンターに入っている個数
		if int(sender.title) > counter.count(menu_place[self]):
			#数字ボタンとカウンターの個数の差
			dif = int(sender.title) - counter.count(menu_place[self])
			#差だけ増やす
			for i in range(dif):
				counter.append(menu_place[self])
						
		#カウンターに入っている個数 > ボタンの数		
		else:
			dif = counter.count(menu_place[self]) - int(sender.title)				
			#差だけ減らす
			for i in range(dif):
				counter.remove(menu_place[self])		
				
			
	counterdisp1.text = counter_disp[0]
	counterdisp2.text = counter_disp[1]
	counterdisp3.text = counter_disp[2]
	counterdisp4.text = counter_disp[3]
		
	
	

	
	
#CLキーのイベント処理
def onClTap(sender):
	sound.play_effect('game:Beep')
	global counter
	
	
	#担当label クリア
	if len(z) > 0:
		if len(z) == 1:
			if not chargelabel.text == '_____':
				chargelabel.text = '_____'
	
	
	
	#disp1上 クリア
	elif len(x) == 0:
		if not disp1.text == '_____':
			disp1.text = '_____'
			
			
			
	#disp2 クリア
	elif len(x) == 1:
		if not disp2.text == '？':
			disp2.text = '？'
	
	
	
	#tableview1[0] クリア
	elif len(x) == 2:
		#初期表示のメニュー？が入っていたらなにもしない
		if not table1.data_source.items[0] == 'メニュー' + ' '*15 + '？':
			#個数を0にする
			table1.data_source.items[0] = menu_place[0]
			counter_disp[0] = '0'
			#カウンターの中の個数を0にする
			counter = [c for c in counter if c != menu_place[0]]
			print(' ')
			print('clを押して0にした')
			print('counter')
			print(counter)
			#個数0のやつができた証拠
			y.append('y')
			counterdisp1.text = counter_disp[0]
			counterdisp2.text = counter_disp[1]
			counterdisp3.text = counter_disp[2]
			counterdisp4.text = counter_disp[3]

			
			
	#tableview1[1] クリア
	elif len(x) == 3:
		ClBtn(sender,1)
	#tableview1[2] クリア
	elif len(x) == 4:
		ClBtn(sender,2)
	#tableview1[3] クリア
	elif len(x) == 5:
		ClBtn(sender,3)

			
	counterdisp1.text = counter_disp[0]
	counterdisp2.text = counter_disp[1]
	counterdisp3.text = counter_disp[2]
	counterdisp4.text = counter_disp[3]


def ClBtn(sender,self):
	global counter
	table1.data_source.items[self] = menu_place[self]
	counter_disp[self] = '0'
	#カウンターの中の個数を0にする
	counter = [c for c in counter if c != menu_place[self]]
	print(' ')
	print('clを押して0にした')
	print('counter')
	print(counter)
	#個数0のやつができた証拠
	y.append('y')

	
	
	
	
	
#↓キーのイベント処理
def onCsrDwnTap(sender):
	sound.play_effect('game:Beep')

	#カーソルが画面外にいかないようにするため
	#tableの要素の数だけ動ける
	len_table = len(table1.data_source.items)
	if len(x) < len_table + 1:
		#label4のときは増やさない
		if len(x) < 5:
			#担当キーが押されてないとき
			if len(z) == 0:
				#リストxに1個追加（上下の判別）
				x.append('x')
				
	CsrDwn(sender)


def CsrDwn(sender):						
	#disp1		
	if len(x) == 0:
		disp1.border_color = 'black'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'white'
	#disp2		
	if len(x) == 1:
		disp1.border_color = '#aaddff'
		disp2.border_color = 'black'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'white'
	#label1
	if len(x)	== 2:
		v.remove_subview(tablenumberlabel)
		v.remove_subview(disp1)
		v.remove_subview(peoplenumberlabel)
		v.remove_subview(disp2)
		v.add_subview(table1)
		v.add_subview(label1)
		v.add_subview(label2)
		v.add_subview(label3)
		v.add_subview(label4)
		v.add_subview(counterdisp1)
		v.add_subview(counterdisp2)
		v.add_subview(counterdisp3)
		v.add_subview(counterdisp4)
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'black'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'white'
	#label2
	if len(x) == 3:
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'black'
		label3.border_color = 'white'
		label4.border_color = 'white'
	#label3
	if len(x) == 4:
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'black'
		label4.border_color = 'white'
	#label4
	if len(x) == 5:
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'black'



	#0の個数のやつが現れた次のアクションで消す
	if len(y) > 0:
		print(' ')
		print('0個のものがあるよ')
		y.clear()
		print('今のcounter')
		print(counter)
		print('今のmenu')
		print(menu_place)
		#menu_placeを1個ずつ取り出す
		for m in menu_place:
			#counterの中にあるかを調べる
			if not m in counter:
				#なかったら、menuとtableから消す
				print(' ')
				print(m + 'が0個だね')
				print(m + 'を消すよ')
				index = menu_place.index(m)
				menu_place.remove(m)
				del table1.data_source.items[index]
				#下になにか要素があるなら
				if len(table1.data_source.items) > 0:
					#個数を上につめる
					for c in range(5-(index+1)):
						counter_disp[index + c] = counter_disp[index + c + 1]
					
				#なにも入ってないとき	
				else:
					#その場所の個数表示を消す
					counter_disp[index] = ''
				print('消したよ')
				print('menu')
				print(menu_place)
				print('table')
				print(table1.data_source.items)
				#tableになにも入っていないなら、メニュー？を追加
				if len(table1.data_source.items) == 0:
						table1.data_source.items.append('メニュー' + ' '*15 + '？')
						

	counterdisp1.text = counter_disp[0]
	counterdisp2.text = counter_disp[1]
	counterdisp3.text = counter_disp[2]
	counterdisp4.text = counter_disp[3]






#↑キーのイベント処理
def onCsrUpTap(sender):
	sound.play_effect('game:Beep')
	
	#disp1のときは消さない
	if len(x) > 0:
		#担当キーが押されてないとき
		if len(z) == 0:
			#リストxの中身を1個消す（上下の判別）
			del x[0]
			
	CsrUp(sender)

def CsrUp(sender):
	#disp1		
	if len(x) == 0:
		disp1.border_color = 'black'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'white'
	#disp2		
	if len(x) == 1:
		v.add_subview(tablenumberlabel)
		v.add_subview(disp1)
		v.add_subview(peoplenumberlabel)
		v.add_subview(disp2)
		v.remove_subview(table1)
		v.remove_subview(label1)
		v.remove_subview(label2)
		v.remove_subview(label3)
		v.remove_subview(label4)
		v.remove_subview(counterdisp1)
		v.remove_subview(counterdisp2)
		v.remove_subview(counterdisp3)
		v.remove_subview(counterdisp4)
		disp1.border_color = '#aaddff'
		disp2.border_color = 'black'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'white'
	#label1
	if len(x)	== 2:
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'black'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'white'	
	#label2
	if len(x) == 3:
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'black'
		label3.border_color = 'white'
		label4.border_color = 'white'
	#label3
	if len(x) == 4:
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'black'
		label4.border_color = 'white'
	#label4
	if len(x) == 5:
		disp1.border_color = '#aaddff'
		disp2.border_color = '#aaddff'
		label1.border_color = 'white'
		label2.border_color = 'white'
		label3.border_color = 'white'
		label4.border_color = 'black'



	#0の個数のやつが現れた次のアクションで消す
	if len(y) > 0:
		print(' ')
		print('0個のものがあるよ')
		y.clear()
		print('今のcounter')
		print(counter)
		print('今のmenu')
		print(menu_place)
		#menu_placeを1個ずつ取り出す
		for m in menu_place:
			#counterの中にあるかを調べる
			if not m in counter:
				#なかったら、menuとtableから消す
				print(' ')
				print(m + 'が0個だね')
				print(m + 'を消すよ')
				index = menu_place.index(m)
				menu_place.remove(m)
				del table1.data_source.items[index]
				#下になにか要素があるなら
				if len(table1.data_source.items) > 0:
					#個数を上につめる
					for c in range(5-(index+1)):
						counter_disp[index + c] = counter_disp[index + c + 1]
				#下になにもないなら	
				else:
					#その場所の個数表示を消す
					counter_disp[index] = ''
				print('消したよ')
				print('menu')
				print(menu_place)
				print('table')
				print(table1.data_source.items)
				#tableになにも入っていないなら、メニュー？を追加
				if len(table1.data_source.items) == 0:
						table1.data_source.items.append('メニュー' + ' '*15 + '？')

												
	counterdisp1.text = counter_disp[0]
	counterdisp2.text = counter_disp[1]
	counterdisp3.text = counter_disp[2]
	counterdisp4.text = counter_disp[3]
	
	
	
	
	
	
#TableViewのイベント処理
def onAction(sender):
	sound.play_effect('game:Beep')
	global counter

	#担当キーが押されてないとき	
	if len(z) == 0:
		Menu(sender)
	
	
def Menu(sender):	
	print(' ')
	print(sender.title + 'を押した')
	
	#0の個数のやつが現れた次のアクションで消す
	if len(y) > 0:
		print(' ')
		print('0個のものがあるよ')
		y.clear()
		print('今のcounter')
		print(counter)
		print('今のmenu')
		print(menu_place)
		#menu_placeを1個ずつ取り出す
		for m in menu_place:
			#counterの中にあるかを調べる
			if not m in counter:
				#なかったら、menuとtableから消す
				print(' ')
				print(m + 'が0個だね')
				#次にくるメニューと一致してたら消さない
				if m == sender.title:
					print('0個だけど消さないよ')
					None
					print('menu')
					print(menu_place)
					print('table')
					print(table1.data_source.items)
					
				else:
					print(m + 'を消すよ')
					index = menu_place.index(m)
					menu_place.remove(m)
					del table1.data_source.items[index]
					#下になにか要素があるなら
					if len(table1.data_source.items) > 0:
						#個数を上につめる
						for c in range(5-(index+1)):
							counter_disp[index + c] = counter_disp[index + c + 1]
					#なにもないなら
					else:
						#その場所の個数表示を消す
						counter_disp[index] = ''
					print('消したよ')
					print('menu')
					print(menu_place)
					print('table')
					print(table1.data_source.items)
					#tableになにも入っていないなら、メニュー？を追加
					if len(table1.data_source.items) == 0:
						table1.data_source.items.append('メニュー' + ' '*15 + '？')
						

	#初期表示のメニュー？が入っていたら消す
	if table1.data_source.items[0] == 'メニュー' + ' '*15 + '？':
		del table1.data_source.items[0]		
	
		
	#sender == 押されたやつを入れる
	#それ以外は、sender.superview で呼び出し
	
	
	#重複があるなら
	if sender.title in menu_place or sender.title in menu_place_storage:
		print('重複あり')
		
		print('重複前')
		print('counter')
		print(counter)
		#重複を数えるため、とりあえず追加
		counter.append(sender.title)
		print('重複後')
		print('counter')
		print(counter)
		#重複リスト
		key_list = Key(counter)
		print('key')
		print(key_list)
		value_list = Value(counter)
		print('value')
		print(value_list)		
		#その注文のやつの場所
		#menuにあって、keyやvalueにないときがある
		#menu ランチ0、お子様1 →key お子様、value1
		print('menu')
		print(menu_place)
		print('counter')
		print(counter)
		print('=')
		print('value')
		print(value_list)
		index = key_list.index(sender.title)		
		#個数
		#key == ボタンの名前 のところのインデックスを取得
		#そのインデックスの場所の個数を取得
		#keyの並びとvalueの並びは同じ
		v = value_list[index]
		
		
		#通常
		#menu_placeに重複があるとき
		#つまり、そのページに重複があるとき
		if sender.title in menu_place:
			#menu == ボタンの名前 のところのインデックスを取得
			#つまり、tableの場所を取得
			index = menu_place.index(sender.title)
			#重複のやつをアップデート
			table1.data_source.items[index] = sender.title
			counter_disp[index] = str(v)
			#カーソル自動移動
			sel = index + 2
			if sel - len(x) > 0:
				for dif in range(sel - len(x)):
					x.append('x')
			else:
				#今いる場所 - 追加場所 だけ削除
				for dif in range(len(x) - sel):
					del x[0]
					
		#2ページ目のとき
		#menu_place_storageに重複があるとき
		#つまり、そのページに重複がないとき
		else:
			print('そのページに重複がないとき')
			#1ページ目に戻す
			#tableview更新（今、4のとき）
			
			#2ページ目のmenu_placeをstorageに保管
			print('menu_place')
			print(menu_place)
			#storageに入っている個数を確認
			len_mps = len(menu_place_storage)
			#storageに追加
			for mps in menu_place[:4]:
				menu_place_storage.append(mps)
			print(menu_place_storage)
			#2ページ目の表示を削除
			print('削除前')
			print(menu_place)
			del menu_place[:4]
			print(menu_place)
			print('削除前')
			print(table1.data_source.items)
			del table1.data_source.items[:4]
			print(table1.data_source.items)
			
			#storageに入ってた個数分だけ呼び出す
			for mp in menu_place_storage[:len_mps]:
				menu_place.append(mp)
				table1.data_source.items.append(mp)
			del menu_place_storage[:len_mps]
			
			
			#counter_dispも同様
			#2ページ目のcounter_dispをstorageに保管
			for cds in counter_disp[:4]:
				counter_disp_storage.append(cds)
			#storageから呼び出し、1ページ目のcounter_dispを表示
			counter_disp[0] = counter_disp_storage[0]
			counter_disp[1] = counter_disp_storage[1]
			counter_disp[2] = counter_disp_storage[2]
			counter_disp[3] = counter_disp_storage[3]
			#storageから1ページ目のcounter_dispを削除
			del counter_disp_storage[:4]
			#追加の重複を更新
			index = menu_place.index(sender.title)
			counter_disp[index] = str(v)			


			#カーソル自動移動
			index = menu_place.index(sender.title)
			sel = index + 2
			if sel - len(x) > 0:
				for dif in range(sel - len(x)):
					x.append('x')
			else:
				#今いる場所 - 追加場所 だけ削除
				for dif in range(len(x) - sel):
					del x[0]


		counterdisp1.text = counter_disp[0]
		counterdisp2.text = counter_disp[1]
		counterdisp3.text = counter_disp[2]
		counterdisp4.text = counter_disp[3]
			
		
		CsrDwn(sender)
		CsrUp(sender)
		
		print(' ')
		print(' ')
		print('結果')
		print(table1.data_source.items)
		print(menu_place)
		print(counter)
		print('menu_place_storage')
		print(menu_place_storage)
		print(' ')

		#menu_placeに追加してないから、menu_placeは変わらない		
				
		
	
	else:
		print('重複なし')
		#tableview1に追加
		table1.data_source.items.append(sender.title)
		print('tableに追加')
		print(table1.data_source.items)
		
		#タイトルだけをリストに入れる
		counter.append(sender.title)
		print('counterに追加')
		print(counter)
		menu_place.append(sender.title)
		print('menuに追加')
		print(menu_place)
		
		#個数を表示
		index = menu_place.index(sender.title)
		counter_disp[index] = '1'
		
		#カーソル自動移動
		sel = index + 2
		#新たな場所 - 今いる場所 だけ追加
		for dif in range(sel - len(x)):
			x.append('x')
		CsrDwn(sender)
		CsrUp(sender)

	
	counterdisp1.text = counter_disp[0]
	counterdisp2.text = counter_disp[1]
	counterdisp3.text = counter_disp[2]
	counterdisp4.text = counter_disp[3]
	
	
	#tableview更新（今、4のとき）
	if len(menu_place) > 4:
		#1ページ目のmenu_placeをstorageに保管
		for mps in menu_place[:4]:
			menu_place_storage.append(mps)
		print('menu_place_storage')
		print(menu_place_storage)
		#menu_placeを全削除	
		#1ページ目の表示を削除
		del menu_place[:4]
		del table1.data_source.items[:4]
		print('menu_place')
		print(menu_place)
		print('表示')
		print(table1.data_source.items)
		
		#新たなリストに保管
		for cds in counter_disp[:4]:
			counter_disp_storage.append(cds)
			
		counter_disp[0] = '1'
		counter_disp[1] = ''
		counter_disp[2] = ''
		counter_disp[3] = ''
		counter_disp[4] = ''
		
		#カーソル自動移動
		index = menu_place.index(sender.title)
		sel = index + 2
		if sel - len(x) > 0:
			for dif in range(sel - len(x)):
				x.append('x')		
		else:
			#今いる場所 - 追加場所 だけ削除
			for dif in range(len(x) - sel):
				del x[0]
		CsrDwn(sender)
		CsrUp(sender)
			
		counterdisp1.text = counter_disp[0]
		counterdisp2.text = counter_disp[1]
		counterdisp3.text = counter_disp[2]
		counterdisp4.text = counter_disp[3]



	

	
#担当キーのイベント処理
def onChargeTap(sender):
	global chargelabel, z
	sound.play_effect('game:Beep')
	
	#担当キーを複数回押したらまずいから
	if len(z) == 0:
		z.append('z')
		
	#送信中は画面を初期化させない	
	if not len(z) == 3:
		#viewへの組み込み(表示)(初期化)
		label.text = '     担当No.  '
		label.alignment = 0
		chargelabel.text = '_____'
		v.add_subview(label)
		v.add_subview(chargelabel)
		v.add_subview(cancelbutton)
		#len(z)==2のときに担当キーを押してもいいように
		z = ['z']



#キャンセルキーのイベント処理
def onCclBtnTap(sender):
	sound.play_effect('game:Beep')
	
	if len(z) == 2:
		label.text = '     担当No.  '
		chargelabel.text = '_____'
		v.add_subview(chargelabel)
		del z[0]
		
	else:
		v.remove_subview(label)
		v.remove_subview(chargelabel)
		v.remove_subview(cancelbutton)
		z.clear()



#送信キーのイベント処理
def onSndBtnTap(sender):
	sound.play_effect('game:Beep')
	
	#数値入力なしでは送信できない
	if not chargelabel.text == '_____':
		z.append('z')
	
	if len(z) == 2:
		label.text = '     担当No.  ' + chargelabel.text + 'でOK？'
		v.remove_subview(chargelabel)

	if len(z) == 3:
		label.text = '送信中…'
		label.alignment = 1
		v.remove_subview(cancelbutton)
		
		th1 = threading.Thread(target = sending1)
		th1.start()
		
		th2 = threading.Thread(target = sending2)
		th2.start()

		
		
		
		
		
#サポート系	
def Key(self):
	key_list = []
	value_list = []
	
	for k, v in collections.Counter(self).items():
			
			#menu_placeと同じ内容
			key_list.append(k)
			#menu_placeと同じ順番の個数
			value_list.append(v)		

	return key_list
	
	
	
def Value(self):
	key_list = []
	value_list = []
	
	for k, v in collections.Counter(self).items():
			
			#menu_placeと同じ内容
			key_list.append(k)
			#menu_placeと同じ順番の個数
			value_list.append(v)
			
	return value_list



#スリープ使うならスレッド内で
#join()とテキスト変更でバグる
def sending1():
	time. sleep(2)
	
	label.text = '担当No. ' + chargelabel.text + 'に変更完了'
	
	

def sending2():
	time.sleep(4)
	
	v.remove_subview(label)
	v.remove_subview(cancelbutton)
	z.clear()
	
	

	
	
	

	
	
	
	
	
	

	

	



#メイン処理
v = ui.load_view()
tablenumberlabel = v['tablenumberlabel']
peoplenumberlabel = v['peoplenumberlabel']
disp1 = v['displaylabel1']
disp2 = v['displaylabel2']
table1 = v['tableview1']
label1 = v['tableviewlabel1']
label2 = v['tableviewlabel2']
label3 = v['tableviewlabel3']
label4 = v['tableviewlabel4']
counterdisp1 = v['counterdisp1']
counterdisp2 = v['counterdisp2']
counterdisp3 = v['counterdisp3']
counterdisp4 = v['counterdisp4']






#動的インスタンスの作成

#担当キー
#画面切り替えlabel
#インスタンスの作成
label = ui.Label()
#表示テキストの設定
label.text = '     担当No.  '
#揃え方 (0,1,2)
label.alignment = 0
#大きさ (横位置,縦位置,横幅,縦幅)
label.bounds = (0, 0, 198, 292)
#中心位置の設定(x、y)
label.center = (105, 152)
label.border_width = 1
label.border_color = 'black'
#背景色
label.background_color = 'white'

#ナンバー入力label
chargelabel = ui.Label()
chargelabel.name = 'chargelabel'
chargelabel.text = '_____'
chargelabel.bounds = (0, 0, 50, 26)
chargelabel.center = (119.5, 152)

#キャンセルbutton
cancelbutton = ui.Button()
cancelbutton.name = 'cancelbutton'
cancelbutton.title = '✗ キャンセル'
cancelbutton.tint_color = 'black'
cancelbutton.bounds = (0, 0, 97, 40)
cancelbutton.background_color = '#cfcfcf'
cancelbutton.border_width = 1
cancelbutton.border_color = 'black'
cancelbutton.center = (54.5, 278)
cancelbutton.action = onCclBtnTap





v.remove_subview(table1)
v.remove_subview(label1)
v.remove_subview(label2)
v.remove_subview(label3)
v.remove_subview(label4)
v.remove_subview(counterdisp1)
v.remove_subview(counterdisp2)
v.remove_subview(counterdisp3)
v.remove_subview(counterdisp4)


v.present('popover', orientations = ['portrait'])