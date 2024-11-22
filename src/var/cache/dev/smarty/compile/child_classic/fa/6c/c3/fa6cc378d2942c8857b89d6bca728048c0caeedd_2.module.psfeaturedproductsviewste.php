<?php
/* Smarty version 3.1.48, created on 2024-11-22 19:00:54
  from 'module:psfeaturedproductsviewste' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_6740c6d654ff97_72576552',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'fa6cc378d2942c8857b89d6bca728048c0caeedd' => 
    array (
      0 => 'module:psfeaturedproductsviewste',
      1 => 1732286125,
      2 => 'module',
    ),
  ),
  'includes' => 
  array (
    'file:catalog/_partials/productlist.tpl' => 1,
  ),
),false)) {
function content_6740c6d654ff97_72576552 (Smarty_Internal_Template $_smarty_tpl) {
?><!-- begin /var/www/html/themes/child_classic/modules/ps_featuredproducts/views/templates/hook/ps_featuredproducts.tpl --><section class="featured-products clearfix">
    Najnowsze zestawy i wzory!
  </h2>
  <?php $_smarty_tpl->_subTemplateRender("file:catalog/_partials/productlist.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('products'=>$_smarty_tpl->tpl_vars['products']->value,'cssClass'=>"row",'productClass'=>"col-xs-12 col-sm-6 col-lg-4 col-xl-3"), 0, false);
?>

</section>

<section class="image_box"  style="margin: 20px;">
        <div class="box" style="width: 100%; height: 200px; background-color: black; border-radius: 20px; color: white; text-align: center;">
        <h1>Placeholder</h1>
        </div>
</secton>

<section class="learn to crochet" style="margin: 20px;">
  <h2 class="learn_title" style="text-align:center;">
    Naucz się szydełkować >
  </h2>
  <h3 class="learn_subtitle" style="text-align:center;">
	Zestawy i wzory dla początkujących, aby rozpocząć twoją przygodę z szydełkiem.
  </h3>
</section>


<section class="seasonal kits"  style="margin: 20px;">
  <h2 class="seasonal_title" style="text-align:center;">
    Zestawy Sezonowe >
  </h2>
  <h3 class="seasonal_subtitle" style="text-align:center;">
       Tematyczne, sezonowe zestawy szydełkowe zawierające materiały dla 6 unikalnych wzorów oraz 3 miesiące Członkowstwa Club Crochet Pattern
  </h3>
</section>

<section class="yellow_box"  style="margin: 20px;">
	<div class="box" style="width: 100%; height: 200px; background-color: #E1A821; border-radius: 20px; color: white;">
	<h2>Club Crochet Roczna Przepustka</h2>
	<h3>Kup roczny zapas sezonowych zestawów dostarczony do twoich drzwi i zaoszczędź 15%!</h3>
	<h3>	24+ projektów szydełkowych</h3>
	<h3>12 miesięcy członkowstwa klubu</h3>
	<h3>Bonusowe przypinki</h3>
	</div>
</secton>

<section class="materials"  style="margin: 20px;">                                                                                   
                     
  <h2 class="materials_title" style="text-align:center;">
    Materiały >
  </h2>
  <h3 class="materials_subtitle" style="text-align:center;">                     
  Zaopatrz się w zapasy, w tym w naszą ekskluzywną włóczkę bawełnianą Club Crochet amigurumi.                
  </h3>

</section>

<section class="merch"  style="margin: 20px;">

  <h2 class="merch_title" style="text-align:center;">
    Produkty >
  </h2>

</section>
<!-- end /var/www/html/themes/child_classic/modules/ps_featuredproducts/views/templates/hook/ps_featuredproducts.tpl --><?php }
}
