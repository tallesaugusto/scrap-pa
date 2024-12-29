from fetch_pa.fetch_pa import fech_data_pa
from fetch_oxxo.fetch_oxxo import fech_data_oxxo
meta_datas = [
    {
        'url': 'https://api.vendas.gpa.digital/pa/special-page',
        'param': 'especialcafe_cafesespeciais',
        'field_parm': 'terms'
    },
    {
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|basico-da-despensa|acucar-e-adocante',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'bebidas',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'bebidas-alcoolicas-',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|carnes-e-aves',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|congelados',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|doces-e-sobremesas',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|basico-da-despensa|farinaceos',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|frios',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|frutas',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|basico-da-despensa|graos-e-cereais',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|basico-da-despensa|sopas-e-cremes',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|legumes-e-verduras',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|frios',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|basico-da-despensa|massas',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|basico-da-despensa|oleos-e-azeites',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|ovos',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|peixaria',
        'field_parm': 'multiCategory'
    },{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|queijos-e-laticinios',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|rotisserie',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|biscoitos-salgadinhos-e-snacks|salgadinhos-e-snacks',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|sementes-e-oleaginosas',
        'field_parm': 'multiCategory'
    },
{
        'url': 'https://api.vendas.gpa.digital/pa/search/category-page',
        'param': 'alimentos|basico-da-despensa|sopas-e-cremes',
        'field_parm': 'multiCategory'
    },



]

def scrap_pao_de_acucao():
    for index, meta_data in enumerate(meta_datas):
        try:
            fech_data_pa(1, meta_data.get('url'), meta_data.get('param'), meta_data.get('field_parm'))
        except Exception as e:
            print(e)

def scrap_oxxo():
    try:
        fech_data_oxxo()
    except Exception as e:
        print(e)
def main():
    scrap_pao_de_acucao()
    scrap_oxxo()


if __name__ == '__main__':
    main()
