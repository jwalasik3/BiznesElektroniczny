// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "DTrackPlugin/Public/DTrackLiveLinkRetargetAsset.h"
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeDTrackLiveLinkRetargetAsset() {}

// Begin Cross Module References
DTRACKPLUGIN_API UClass* Z_Construct_UClass_UDTrackLiveLinkRetargetAsset();
DTRACKPLUGIN_API UClass* Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_NoRegister();
LIVELINKANIMATIONCORE_API UClass* Z_Construct_UClass_ULiveLinkRetargetAsset();
UPackage* Z_Construct_UPackage__Script_DTrackPlugin();
// End Cross Module References

// Begin Class UDTrackLiveLinkRetargetAsset
void UDTrackLiveLinkRetargetAsset::StaticRegisterNativesUDTrackLiveLinkRetargetAsset()
{
}
IMPLEMENT_CLASS_NO_AUTO_REGISTRATION(UDTrackLiveLinkRetargetAsset);
UClass* Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_NoRegister()
{
	return UDTrackLiveLinkRetargetAsset::StaticClass();
}
struct Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics
{
#if WITH_METADATA
	static constexpr UECodeGen_Private::FMetaDataPairParam Class_MetaDataParams[] = {
		{ "BlueprintType", "true" },
		{ "Comment", "/**\n * DTrack LiveLink remapping asset\n */" },
		{ "IncludePath", "DTrackLiveLinkRetargetAsset.h" },
		{ "IsBlueprintBase", "true" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkRetargetAsset.h" },
		{ "ToolTip", "DTrack LiveLink remapping asset" },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_bRotationOnly_MetaData[] = {
		{ "Category", "DTrack Retargeting Asset" },
		{ "DisplayName", "Use Rotation Only" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkRetargetAsset.h" },
		{ "ToolTip", "Set this to move every bone to the positions of its representation in the reference skeleton. Results in no gaps between bones. Fingers might overlap." },
	};
	static constexpr UECodeGen_Private::FMetaDataPairParam NewProp_BoneNameMap_MetaData[] = {
		{ "Category", "DTrack Retargeting Asset" },
		{ "Comment", "/**\n\x09* Used to remap skeletons bone names if they are different. (Left = bones to remap; Right = Correct bone name)\n\x09*/" },
		{ "ModuleRelativePath", "Public/DTrackLiveLinkRetargetAsset.h" },
		{ "ToolTip", "Used to remap skeletons bone names if they are different. (Left = bones to remap; Right = Correct bone name)" },
	};
#endif // WITH_METADATA
	static void NewProp_bRotationOnly_SetBit(void* Obj);
	static const UECodeGen_Private::FBoolPropertyParams NewProp_bRotationOnly;
	static const UECodeGen_Private::FNamePropertyParams NewProp_BoneNameMap_ValueProp;
	static const UECodeGen_Private::FNamePropertyParams NewProp_BoneNameMap_Key_KeyProp;
	static const UECodeGen_Private::FMapPropertyParams NewProp_BoneNameMap;
	static const UECodeGen_Private::FPropertyParamsBase* const PropPointers[];
	static UObject* (*const DependentSingletons[])();
	static constexpr FCppClassTypeInfoStatic StaticCppClassTypeInfo = {
		TCppClassTypeTraits<UDTrackLiveLinkRetargetAsset>::IsAbstract,
	};
	static const UECodeGen_Private::FClassParams ClassParams;
};
void Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_bRotationOnly_SetBit(void* Obj)
{
	((UDTrackLiveLinkRetargetAsset*)Obj)->bRotationOnly = 1;
}
const UECodeGen_Private::FBoolPropertyParams Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_bRotationOnly = { "bRotationOnly", nullptr, (EPropertyFlags)0x0010000000000001, UECodeGen_Private::EPropertyGenFlags::Bool | UECodeGen_Private::EPropertyGenFlags::NativeBool, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, sizeof(bool), sizeof(UDTrackLiveLinkRetargetAsset), &Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_bRotationOnly_SetBit, METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_bRotationOnly_MetaData), NewProp_bRotationOnly_MetaData) };
const UECodeGen_Private::FNamePropertyParams Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_BoneNameMap_ValueProp = { "BoneNameMap", nullptr, (EPropertyFlags)0x0000000000000001, UECodeGen_Private::EPropertyGenFlags::Name, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, 1, METADATA_PARAMS(0, nullptr) };
const UECodeGen_Private::FNamePropertyParams Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_BoneNameMap_Key_KeyProp = { "BoneNameMap_Key", nullptr, (EPropertyFlags)0x0000000000000001, UECodeGen_Private::EPropertyGenFlags::Name, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, 0, METADATA_PARAMS(0, nullptr) };
const UECodeGen_Private::FMapPropertyParams Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_BoneNameMap = { "BoneNameMap", nullptr, (EPropertyFlags)0x0010000000000001, UECodeGen_Private::EPropertyGenFlags::Map, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(UDTrackLiveLinkRetargetAsset, BoneNameMap), EMapPropertyFlags::None, METADATA_PARAMS(UE_ARRAY_COUNT(NewProp_BoneNameMap_MetaData), NewProp_BoneNameMap_MetaData) };
const UECodeGen_Private::FPropertyParamsBase* const Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::PropPointers[] = {
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_bRotationOnly,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_BoneNameMap_ValueProp,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_BoneNameMap_Key_KeyProp,
	(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::NewProp_BoneNameMap,
};
static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::PropPointers) < 2048);
UObject* (*const Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::DependentSingletons[])() = {
	(UObject* (*)())Z_Construct_UClass_ULiveLinkRetargetAsset,
	(UObject* (*)())Z_Construct_UPackage__Script_DTrackPlugin,
};
static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::DependentSingletons) < 16);
const UECodeGen_Private::FClassParams Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::ClassParams = {
	&UDTrackLiveLinkRetargetAsset::StaticClass,
	nullptr,
	&StaticCppClassTypeInfo,
	DependentSingletons,
	nullptr,
	Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::PropPointers,
	nullptr,
	UE_ARRAY_COUNT(DependentSingletons),
	0,
	UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::PropPointers),
	0,
	0x001000A0u,
	METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::Class_MetaDataParams), Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::Class_MetaDataParams)
};
UClass* Z_Construct_UClass_UDTrackLiveLinkRetargetAsset()
{
	if (!Z_Registration_Info_UClass_UDTrackLiveLinkRetargetAsset.OuterSingleton)
	{
		UECodeGen_Private::ConstructUClass(Z_Registration_Info_UClass_UDTrackLiveLinkRetargetAsset.OuterSingleton, Z_Construct_UClass_UDTrackLiveLinkRetargetAsset_Statics::ClassParams);
	}
	return Z_Registration_Info_UClass_UDTrackLiveLinkRetargetAsset.OuterSingleton;
}
template<> DTRACKPLUGIN_API UClass* StaticClass<UDTrackLiveLinkRetargetAsset>()
{
	return UDTrackLiveLinkRetargetAsset::StaticClass();
}
DEFINE_VTABLE_PTR_HELPER_CTOR(UDTrackLiveLinkRetargetAsset);
UDTrackLiveLinkRetargetAsset::~UDTrackLiveLinkRetargetAsset() {}
// End Class UDTrackLiveLinkRetargetAsset

// Begin Registration
struct Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkRetargetAsset_h_Statics
{
	static constexpr FClassRegisterCompiledInInfo ClassInfo[] = {
		{ Z_Construct_UClass_UDTrackLiveLinkRetargetAsset, UDTrackLiveLinkRetargetAsset::StaticClass, TEXT("UDTrackLiveLinkRetargetAsset"), &Z_Registration_Info_UClass_UDTrackLiveLinkRetargetAsset, CONSTRUCT_RELOAD_VERSION_INFO(FClassReloadVersionInfo, sizeof(UDTrackLiveLinkRetargetAsset), 887128597U) },
	};
};
static FRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkRetargetAsset_h_2990288185(TEXT("/Script/DTrackPlugin"),
	Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkRetargetAsset_h_Statics::ClassInfo, UE_ARRAY_COUNT(Z_CompiledInDeferFile_FID_Users_DEV_9_Downloads_UnrealDTrackPlugin_master_55_DTrackPlugin_HostProject_Plugins_DTrackPlugin_Source_DTrackPlugin_Public_DTrackLiveLinkRetargetAsset_h_Statics::ClassInfo),
	nullptr, 0,
	nullptr, 0);
// End Registration
PRAGMA_ENABLE_DEPRECATION_WARNINGS
