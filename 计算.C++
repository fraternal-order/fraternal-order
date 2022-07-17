#include<iostream>
using namespace std;
 
 
int main() {
 
    double choice = 0;
    double choice1 = 0;
    double choice2 = 0;
    double choice3 = 0;
    double choice4 = 0;
     
    FLAG:
    cout << "请输入需要计算的类型" << endl;
    cout << "1.面积" << endl;
    cout << "2.体积" << endl;
    cout << "3.表面积" << endl;
    cout << "4.周长" << endl;
 
    cin >> choice;
    if (choice == 1)
    {//面积
        cout << "请输入需要计算的图形" << endl;
        cout << "1.正方形" << endl;
        cout << "2.长方形" << endl;
        cout << "3.圆形" << endl;
        cout << "4.平行四边形" << endl;
        cout << "5.梯形" << endl;
        cout << "6.三角形形" << endl;
        cin >> choice1;
        if (choice1 == 1) //正方形的面积
        {
            cout << "请输入正方形的边长" << endl;
            double Sidelength = 0;
            double themeasureofarea = 0;
            cin >> Sidelength;
            cout << "正方形的边长为： " << Sidelength << endl;
            themeasureofarea = Sidelength * Sidelength;
            cout << "正方形的面积为： " << themeasureofarea << endl;
            goto FLAG;
        }
        else if (choice1 == 2) //长方形的面积
        {
            cout << "请输入长方形的长" << endl;
            double edge = 0;
            double wide = 0;
            double themeasureofarea = 0;
            cin >> edge;
            cout << "长方形的长为： " << edge << endl;
            cout << "请输入长方形的宽" << endl;
            cin >> wide;
            cout << "长方形的宽为： " << wide << endl;
            themeasureofarea = edge * wide;
            cout << "长方形的面积为： " << themeasureofarea << endl;
            goto FLAG;
        }
        else if (choice1 == 3) //圆形的面积
        {
            double radius = 0;
            double themeasureofarea = 0;
            cout << "请输入圆的半径" << endl;
            cin >> radius;
            cout << "圆的半径为： " << radius << endl;
            themeasureofarea = radius * radius * 3.14;
            cout << "圆的面积为： " << themeasureofarea << endl;
            goto FLAG;
        }
        else if (choice1 == 4) //平行四边形面积
        {
            double Sidelength = 0;
            double high = 0;
            double themeasureofarea = 0;
            cout << "请输入平行四边形的高" << endl;
            cin >> high;
            cout << "平行四边形的高为： " << high << endl;
            cout << "请输入平行四边形的边长： " << endl;
            cin >> Sidelength;
            cout << "平行四边形的边长为： " << Sidelength << endl;
            themeasureofarea = high * Sidelength;
            cout << "平行四边形的面积为： " << themeasureofarea << endl;
            goto FLAG;
        }
        else if (choice1 == 5) //梯形的面积
        {
            double Upperbottom = 0;
            double mapoutthecourseofactionbeforehand = 0;
            double high = 0;
            double themeasureofarea = 0;
            cout << "请输入梯形的上底" << endl;
            cin >> Upperbottom;
            cout << "梯形的上底为： " << Upperbottom << endl;
            cout << "请输入梯形的下底" << endl;
            cin >> mapoutthecourseofactionbeforehand;
            cout << "梯形的下底为： " << mapoutthecourseofactionbeforehand << endl;
            cout << "请输入梯形的高" << endl;
            cin >> high;
            cout << "梯形的高为： " << endl;
            themeasureofarea = (Upperbottom + mapoutthecourseofactionbeforehand) * high / 2;
            cout << "梯形的面积为： " << themeasureofarea << endl;
            goto FLAG;
        }
        else if (choice1 == 6) //三角形的面积
        {
            double bottom = 0;
            double high = 0;
            double themeasureofarea = 0;
            cout << "请输入三角形的底" << endl;
            cin >> bottom;
            cout << "三角形的底为： " << bottom << endl;
            cout << "请输入三角形的高" << endl;
            cin >> high;
            cout << "三角形的高为： " << high << endl;
            themeasureofarea = bottom * high / 2;
            cout << "三角形的面积为： " << themeasureofarea << endl;
            goto FLAG;
        }
        else
        {
            cout << "输入错误，请重新输入" << endl;
            goto FLAG;
        }
    }
    else if (choice == 2)
    {//体积
        cout << "请输入需要计算的图形" << endl;
        cout << "1.正方体" << endl;
        cout << "2.长方体" << endl;
        cout << "3.圆柱" << endl;
        cout << "4.圆锥" << endl;
        cin >> choice2;
        if (choice2 == 1) //正方体的体积
        {
            double Sidelength = 0;
            double volume = 0;
            cout << "请输入正方体的边长" << endl;
            cin >> Sidelength;
            cout << "正方体的边长为： " << Sidelength << endl;
            volume = Sidelength * Sidelength * Sidelength;
            cout << "正方体的体积为： " << volume << endl;
            goto FLAG;
        }
        else if (choice2 == 2) //长方体的体积
        {
            double edge = 0;
            double wide = 0;
            double high = 0;
            double volume = 0;
            cout << "请输入长方体的长" << endl;
            cin >> edge;
            cout << "长方体的长为： " << edge << endl;
            cout << "请输入长方体的宽" << endl;
            cin >> wide;
            cout << "长方体的宽为： " << wide << endl;
            cout << "请输入长方体的高" << endl;
            cin >> high;
            cout << "长方体的高为： " << high << endl;
            volume = edge * wide * high;
            cout << "长方体的体积为： " << volume << endl;
            goto FLAG;
        }
        else if (choice2 == 3) //圆柱的体积
        {
            double Sidelength = 0;
            double high = 0;
            double volume = 0;
            cout << "请输入圆柱的底面半径" << endl;
            cin >> Sidelength;
            cout << "圆柱的底面半径为： " << Sidelength << endl;
            cout << "请输入圆柱的高" << endl;
            cin >> high;
            cout << "圆柱的高为： " << high << endl;
            volume = Sidelength * Sidelength * 3.14 * high;
            cout << "圆柱的体积为：" << volume << endl;
            goto FLAG;
        }
        else if (choice2 == 4) //圆锥的体积
        {
            double Sidelength = 0;
            double high = 0;
            double volume = 0;
            cout << "请输入圆锥的底面半径" << endl;
            cin >> Sidelength;
            cout << "圆锥的底面半径为： " << Sidelength << endl;
            cout << "请输入圆锥的高" << endl;
            cin >> high;
            cout << "圆锥的高为： " << high << endl;
            volume = Sidelength * Sidelength * 3.14 * high / 3;
            cout << "圆锥的体积为：" << volume << endl;
            goto FLAG;
        }
        else
        {
            cout << "输入错误，请重新输入" << endl;
            goto FLAG;
        }
 
    }
    else if (choice == 3)
    {//表面积
        cout << "请输入需要计算的图形" << endl;
        cout << "1.正方体" << endl;
        cout << "2.长方体" << endl;
        cout << "3.圆锥" << endl;
        cout << "4.圆柱" << endl;
        cin >> choice3;
        if (choice3 == 1) //正方体的表面积
        {
            double Sidelength = 0;
            double Surfacearea = 0;
            cout << "请输入正方体的边长" << endl;
            cin >> Sidelength;
            cout << "正方体的边长为： " << Sidelength << endl;
            Surfacearea = Sidelength * Sidelength * 6;
            cout << "正方体的表面积为： " << Surfacearea << endl;
            goto FLAG;
        }
        else if (choice3 == 2) //长方体的表面积
        {
            double edge = 0;
            double wide = 0;
            double high = 0;
            double Surfacearea = 0;
            cout << "请输入长方体的长" << endl;
            cin >> edge;
            cout << "长方体的长为： " << edge << endl;
            cout << "请输入长方体的宽" << endl;
            cin >> wide;
            cout << "长方体的宽为： " << wide << endl;
            cout << "请输入长方体的高" << endl;
            cin >> high;
            cout << "长方体的高为： " << high << endl;
            Surfacearea = edge * wide * 2 + edge * high * 2 + wide * high * 2;
            cout << "长方体的表面积为： " << Surfacearea << endl;
            goto FLAG;
        }
        else if (choice3 == 3) //圆锥的表面积
        {
            double edge = 0;
            double abusorbusbar = 0;
            double Surfacearea = 0;
            cout << "请输入圆锥的底面半径" << endl;
            cin >> edge;
            cout << "圆锥的底面半径为： " << edge << endl;
            cout << "请输入母线" << endl;
            cin >> abusorbusbar;
            cout << "圆锥的母线为： " << endl;
            Surfacearea = edge * edge * 3.14 + edge * abusorbusbar * 3.14;
            cout << "圆锥的侧面积为： " << Surfacearea << endl;
            goto FLAG;
        }
        else if (choice3 == 4) //圆柱的表面积
        {
            double edge = 0;
            double high = 0;
            double Surfacearea = 0;
            cout << "请输入圆柱的底面半径" << endl;
            cin >> edge;
            cout << "圆柱的底面半径为： " << endl;
            cout << "请输入圆柱的高" << endl;
            cin >> high;
            cout << "圆柱的高为： " << high << endl;
            Surfacearea = edge * edge * 3.14 * 2 + edge * 2 * 3.14 * high;
            cout << "圆柱的表面积为： " << Surfacearea << endl;
            goto FLAG;
        }
        else
        {
            cout << "输入错误，请重新输入" << endl;
            goto FLAG;
        }
    }
    else if (choice == 4)
    {//周长
    cout << "请输入需要计算的图形" << endl;
    cout << "1.正方形" << endl;
    cout << "2.长方形" << endl;
    cout << "3.圆形" << endl;
    cin >> choice4;
        if(choice4==1)  //正方形的周长
        {
            double Sidelength = 0;
            double Perimeter = 0;
            cout << "请输入正方形的边长" << endl;
            cin >> Sidelength;
            cout << "正方形的边长为： " << Sidelength << endl;
            Perimeter = Sidelength * 4;
            cout << "正方形的周长为： " << Perimeter << endl;
            goto FLAG;
        }
        else if (choice4 == 2) //长方形的周长
        {
            double edge = 0;
            double wide = 0;
            double Perimeter = 0;
            cout << "请输入长方形的长" << endl;
            cin >> edge;
            cout << "长方形的长为： " << edge << endl;
            cout << "请输入长方形的宽" << wide << endl;
            cin >> wide;
            cout << "长方形的宽为： " << endl;
            Perimeter = 2 * edge + 2 * wide;
            cout << "长方形的周长为： " << Perimeter << endl;
            goto FLAG;
        }
        else if (choice4 == 3) //圆形的周长
        {
            double radius = 0;
            double Perimeter = 0;
            cout << "请输入圆的半径" << endl;
            cin >> radius;
            cout << "圆的半径为: " << radius << endl;
            Perimeter = radius * 2 * 3.14;
            cout << "圆的周长为： " << Perimeter << endl;
            goto FLAG;
        }
        else
        {
            cout << "输入错误，请重新输入" << endl;
            goto FLAG;
        }
    }
    else
    {
        cout << "输入错误，请重新输入" << endl;
        goto FLAG;
    }
 
    system("pause");
 
    return 0;
}
