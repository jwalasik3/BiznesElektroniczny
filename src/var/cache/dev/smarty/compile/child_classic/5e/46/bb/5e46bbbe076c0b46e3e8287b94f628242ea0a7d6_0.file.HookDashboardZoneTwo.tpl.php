<?php
/* Smarty version 3.1.48, created on 2024-12-05 21:35:59
  from '/var/www/html/modules/ps_metrics/views/templates/hook/HookDashboardZoneTwo.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_67520eaf5419a6_42992766',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '5e46bbbe076c0b46e3e8287b94f628242ea0a7d6' => 
    array (
      0 => '/var/www/html/modules/ps_metrics/views/templates/hook/HookDashboardZoneTwo.tpl',
      1 => 1733430188,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_67520eaf5419a6_42992766 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="metrics-app"></div>

<?php if ($_smarty_tpl->tpl_vars['useLocalVueApp']->value == false) {?>
  <link rel="stylesheet" href="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathAssetsCdn']->value ));?>
" type="text/css" media="all">
<?php } elseif ($_smarty_tpl->tpl_vars['useLocalVueApp']->value == true && $_smarty_tpl->tpl_vars['useBuildModeOnly']->value == true) {?>
  <link rel="stylesheet" href="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathAssetsBuilded']->value ));?>
" type="text/css" media="all">
<?php }?>

<?php if ($_smarty_tpl->tpl_vars['useLocalVueApp']->value == true) {?>
  <?php if ($_smarty_tpl->tpl_vars['useBuildModeOnly']->value == true) {?>
    <?php echo '<script'; ?>
 type="module" src="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathAppBuilded']->value,'htmlall','UTF-8' ));?>
"><?php echo '</script'; ?>
>
  <?php } else { ?>
    <?php echo '<script'; ?>
 type="module" src="https://localhost:3001/@vite/client"><?php echo '</script'; ?>
>
    <?php echo '<script'; ?>
 type="module" src="https://localhost:3001/src/main.ts"><?php echo '</script'; ?>
>
  <?php }
} else { ?>
  <?php echo '<script'; ?>
 type="module" src="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['pathAppCdn']->value,'htmlall','UTF-8' ));?>
"><?php echo '</script'; ?>
>
<?php }
}
}