<?php
/* Smarty version 3.1.48, created on 2024-12-05 21:36:02
  from '/var/www/html/admin282oxerj0/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_67520eb2d5e498_02117655',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '9c8d13909fdeb445816e100b67a65764df3bd6bf' => 
    array (
      0 => '/var/www/html/admin282oxerj0/themes/default/template/content.tpl',
      1 => 1733430160,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_67520eb2d5e498_02117655 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
