// yingshaoxo: Though this is my first cpp program, but I recommend you use pure c99 to write programs. And also, use English!
// It is written in high school. At that time I do not know English yet.
#include<iostream>				// I/O流
#include <fstream>				// 文件流
#include<string>				// string字符
#include<time.h>				// 时间
#include<sstream>				// 超级流
#include<stdlib.h>				// atoi()

using namespace std;

string shezhidizhi = "setting.txt";
const string zhuangtai = "非调试";

void firstshezhi();
string xuanze();
string xie();
string duqu(string & dizhi);
void cunru(string & x, string & allshu, string & dizhi);
void sdshezhi();
string kanshezhi(int x);
void xieshezhi(int x, string wen);
void fengexian(int x);
string gettime();
string intgetstring(const int n);
int stringgetint(const string str);


void clear_screen() {
    fengexian(20);
    cout << "\n\n";
    }


int main()
{
	cout << "Welcome！\n\n";

	firstshezhi();


  start:

	string jishidizhi = kanshezhi(1);	// 文本地址
	string rijimoshi = kanshezhi(0);	// 是否开启日记模式

	clear_screen();

	string what(xuanze());

	if (what == "l")
	{
		string txt(duqu(jishidizhi));
		cout << jishidizhi << endl << txt;

	}


	if (what == "w")
	{
		string a(duqu(jishidizhi));
		if (rijimoshi == "yes")
		{
			string qianwen = duqu(jishidizhi);

			if (qianwen.find(gettime()) == qianwen.npos)
				a += "\n\n" + gettime();

		}
		string b(xie());
		cunru(a, b, jishidizhi);

	}


	if (what == "q")
	{
		exit(0);
	}


	if (what == "setting")
	{
		sdshezhi();
	}


	if (what == "destroy")
	{
		what = "";
		cout << "\nDestroy all the text？(y/n)\n";
		cin >> what;
		if (what == "y")
		{
			string x;
			cunru(x, x, jishidizhi);
			cout << "\nText destroyed！";
		}

	}


	fengexian(20);
	cout << "\n\nReturn the menu？(y/n)\n";

	string yf;
	cin >> yf;
	if (yf == "y")
	{
		clear_screen();
		goto start;
	}
	else
	{
		cout << endl << "Please quit directly！";
	}

}



void firstshezhi()
{

	if (kanshezhi(2) != "Not first")
	{

        xieshezhi(1, "my diary.txt");
        
        string shit;
        shit = "my diary.txt";
		string y;
		cunru(y, y, shit);

		xieshezhi(0, "yes");
		xieshezhi(2, "Not first");

	}

}




void sdshezhi()
{
	string x;
	cout << "\nDiary or noy？(y/n)\n";
	cin >> x;
	if (x == "y")
		xieshezhi(0, "yes");
	else
		xieshezhi(0, "no");

	x = "";
	cout << "\nStorage address?(Typing x to use the default \"my diary.txt\"):\n";
	cin >> x;
	if (x == "x")
		xieshezhi(1, "my diary.txt");
	else
		xieshezhi(1, x);

	cout << "\nOK！\n";


}





string xuanze()
{
	string b;

	do
	{
                const char *text = "'l' is for look\n'w' is for write\n'q' is for quit\n'setting' and 'destroy' also can be using";
		cout << text << endl;
		
		cin >> b;
	}
	while (b != "l" && b != "w" && b != "q" && b != "setting" && b != "destroy");

	clear_screen();
	cout << "You choose——" << b << "!\n";
	fengexian(20);

	return b;

}




string xie()
{
  kaixie:
	cout << "Please typing and finish it by enter #:\n(New typing use @)\n";

	string allw;
	char w;
	cin.get(w);

	while (w != '#' && w != '@')
	{
		allw += w;
		if (zhuangtai == "非调试")
			w = '\0';			// 调试时可屏蔽
		cout << w;
		cin.get(w);
	}

	if (w == '@')
	{
		clear_screen();
		goto kaixie;
	}

	if (allw == "\n")
		allw = "";

	cout << "\n\nOK！\n";

	return allw;

}




string duqu(string & dizhi)
{
	string x;

	ifstream du(dizhi);

	if (du.good())
	{
		char ch;
		while (du.get(ch))
			x += ch;
		du.close();
	}
	else
	{
		cout << "\nCan't tead the txt！";
	}

	return x;

}




void cunru(string & x, string & allshu, string & dizhi)
{
	ofstream xie(dizhi);

	if (xie.good())
	{
		xie << x + allshu;
		xie.close();
		cout << "\n\nSave as:\n" << x + allshu;
	}
	else
	{
		cout << "\nCan't read and save it！";
	}

}




string kanshezhi(int x)
{

	struct szjg
	{
		string xiang;
		string zhi;
	};

	szjg a[100];

	ifstream dusz(shezhidizhi);
	int shu = 0;

	do
	{
		getline(dusz, a[shu].xiang, ':');
		getline(dusz, a[shu].zhi, '\n');

		++shu;

	}
	while (dusz);

	dusz.close();

	return a[x].zhi;

}





void xieshezhi(int x, string wen)
{

	struct szjg
	{
		string xiang;
		string zhi;
	};
	szjg a[100];

	ifstream dusz(shezhidizhi);
	int shu = 0;

	do
	{
		getline(dusz, a[shu].xiang, ':');
		getline(dusz, a[shu].zhi, '\n');

		++shu;

	}
	while (dusz);

	dusz.close();


	a[x].zhi = wen;
	string shewen;
	for (int q = 0; q < 99; ++q)
	{
		shewen += a[q].xiang;
		shewen += ":";
		shewen += a[q].zhi;
		shewen += "\n";

	}

	ofstream ru(shezhidizhi);
	ru << shewen;

	ru.close();


}





void fengexian(int x)
{

	cout << endl;
	for (int i = 0; i < x; i++)
		cout << "-";
	cout << endl;

}





string gettime()
{
	struct tm shijian;
	time_t t = time(0);
	shijian = *localtime(&t);
	string riqi;
	string nian, yue, ri;
	nian = intgetstring(shijian.tm_year + 1900);
	yue = intgetstring(shijian.tm_mon + 1);
	ri = intgetstring(shijian.tm_mday);
	riqi += nian;
	riqi += "年";
	riqi += yue;
	riqi += "月";
	riqi += ri;
	riqi += "日";

	return riqi;

}




string intgetstring(const int n)
{
	stringstream newstr;
	newstr << n;
	return newstr.str();

}




int stringgetint(const string str)
{
	return atoi(str.c_str());

}
